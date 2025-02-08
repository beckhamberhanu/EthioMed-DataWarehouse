from sqlalchemy.orm import Session
from . import models, schemas

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()

def get_detections(db: Session, confidence: float = 0.5, skip: int = 0, limit: int = 100):
    return db.query(models.DetectionResult)\
            .filter(models.DetectionResult.confidence >= confidence)\
            .offset(skip).limit(limit).all()