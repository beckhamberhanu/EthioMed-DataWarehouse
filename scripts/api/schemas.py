from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    id: int
    message_id: int
    channel: str
    text: str  # Matches DB column name (was cleaned_text)
    date: datetime  # Matches DB column name (was message_date)
    media_path: str | None  # Allow NULL values

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