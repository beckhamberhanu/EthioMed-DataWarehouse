from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    message_id: int
    channel: str
    cleaned_text: str
    message_date: datetime
    media_path: str

    class Config:
        orm_mode = True

class DetectionResultBase(BaseModel):
    image_path: str
    class_label: str
    confidence: float
    bbox: list[int]
    detection_date: datetime

    class Config:
        orm_mode = True

# Explicit exports
__all__ = ["MessageBase", "DetectionResultBase"]