from sqlalchemy import Column, Integer, String, DateTime, Text, JSON, Float
from .database import Base

class Message(Base):
    __tablename__ = "raw_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer)  # Matches message_id column
    channel = Column(String(255))  # Character varying(255)
    text = Column(Text)            # Matches text column (not cleaned_text)
    date = Column(DateTime)        # timestamp without time zone
    media_path = Column(String(255))


class DetectionResult(Base):
    __tablename__ = "detection_results"
    
    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String)
    detection_date = Column(DateTime)
    class_label = Column(String)
    confidence = Column(Float)
    bbox = Column(JSON)