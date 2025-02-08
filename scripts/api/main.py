from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from .crud import get_messages, get_detections
from . import models
from .schemas import MessageBase, DetectionResultBase

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/messages/", response_model=list[schemas.MessageBase])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, skip=skip, limit=limit)
    return messages

@app.get("/detections/", response_model=list[schemas.DetectionResultBase])
def read_detections(
    confidence: float = 0.5,
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    detections = crud.get_detections(db, confidence=confidence, skip=skip, limit=limit)
    return detections

@app.get("/health")
def health_check():
    return {"status": "healthy"}