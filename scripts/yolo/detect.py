import os
import cv2
import torch
import logging
from pathlib import Path
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import DateTime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/yolo_detection.log'),
        logging.StreamHandler()
    ]
)

# Database setup
Base = declarative_base()
engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)

class DetectionResult(Base):
    __tablename__ = 'detection_results'
    
    id = Column(Integer, primary_key=True)
    image_path = Column(String)
    detection_date = Column(DateTime, default=datetime.now)
    class_label = Column(String)
    confidence = Column(Float)
    bbox = Column(JSON)  # Stores [x1, y1, x2, y2] as list

Base.metadata.create_all(engine)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_objects(image_path: str):
    try:
        # Run inference
        img = cv2.imread(image_path)
        results = model(img)
        
        # Parse results
        detections = results.pandas().xyxy[0]
        
        # Store in database
        session = Session()
        for _, row in detections.iterrows():
            detection = DetectionResult(
                image_path=str(image_path),
                class_label=row['name'],
                confidence=round(row['confidence'], 4),
                bbox=[
                    int(row['xmin']),
                    int(row['ymin']),
                    int(row['xmax']),
                    int(row['ymax'])
                ]
            )
            session.add(detection)
        session.commit()
        
        logging.info(f"Processed {image_path} with {len(detections)} detections")
        
    except Exception as e:
        logging.error(f"Error processing {image_path}: {str(e)}")

if __name__ == "__main__":
    image_dir = Path("data/yolo_dataset/images")
    for img_path in image_dir.glob("*.jpg"):
        detect_objects(str(img_path))