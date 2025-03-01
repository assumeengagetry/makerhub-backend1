from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class EventBase(BaseModel):
    event_id: str
    event_name: str
    poster: Optional[str]
    description: str
    location: str
    link: Optional[str]
    start_time: datetime
    end_time: datetime
    registration_deadline: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    event_name: Optional[str] = None
    poster: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    link: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    registration_deadline: Optional[datetime] = None

class EventInDB(EventBase):
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True