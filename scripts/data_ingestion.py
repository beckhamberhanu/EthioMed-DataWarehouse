import os
import logging
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv
import psycopg2
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/scraping.log'),
        logging.StreamHandler()
    ]
)

load_dotenv()

class TelegramScraper:
    def __init__(self):
        self.api_id = os.getenv('TELEGRAM_API_ID')
        self.api_hash = os.getenv('TELEGRAM_API_HASH')
        self.telegram_phone = os.getenv('TELEGRAM_PHONE')
        self.db_conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        
        # Create tables if not exists
        self._create_tables()

    def _create_tables(self):
        with self.db_conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS raw_messages (
                    id SERIAL PRIMARY KEY,
                    message_id INTEGER,
                    channel VARCHAR(255),
                    text TEXT,
                    date TIMESTAMP,
                    media_path VARCHAR(255)
                )
            ''')
            self.db_conn.commit()

    def scrape_channel(self, channel_url, limit=1000):
        try:
            with TelegramClient('session_name', self.api_id, self.api_hash, self.telegram_phone) as client:
                for message in client.iter_messages(channel_url, limit=limit):
                    self._process_message(channel_url, message)
                    
        except Exception as e:
            logging.error(f"Error scraping {channel_url}: {str(e)}")

    def _process_message(self, channel, message):
        try:
            media_path = None
            if message.media and isinstance(message.media, MessageMediaPhoto):
                media_path = self._download_media(message)
                
            with self.db_conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO raw_messages 
                    (message_id, channel, text, date, media_path)
                    VALUES (%s, %s, %s, %s, %s)
                ''', (
                    message.id,
                    channel,
                    message.text,
                    message.date,
                    media_path
                ))
                self.db_conn.commit()
                
            logging.info(f"Processed message {message.id} from {channel}")

        except Exception as e:
            logging.error(f"Error processing message {message.id}: {str(e)}")

    def _download_media(self, message):
        os.makedirs('data/raw/images', exist_ok=True)
        filename = f"data/raw/images/{message.id}.jpg"
        message.download_media(file=filename)
        return filename

if __name__ == "__main__":
    scraper = TelegramScraper()
    
    # Medical text channels
    text_channels = [
        'https://t.me/DoctorsET',
        'https://t.me/yetenaweg',
        'https://t.me/EAHCI'
    ]
    
    # Image channels for YOLO
    image_channels = [
        'https://t.me/CheMed123',
        'https://t.me/lobelia4cosmetics'
    ]
    
    for channel in text_channels + image_channels:
        logging.info(f"Starting scrape for {channel}")
        scraper.scrape_channel(channel, limit=500)