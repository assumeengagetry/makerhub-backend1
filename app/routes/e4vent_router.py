from fastapi import APIRouter, HTTPException
from app.models.e4vent_model import Event
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class EventCreate(BaseModel):
    event_id: str
    event_name: str
    poster: Optional[str] = None
    description: str
    location: str
    link: Optional[str] = None
    start_time: datetime
    end_time: datetime
    registration_deadline: datetime

@router.post("/event")
async def create_event(event: EventCreate):
    new_event = await Event(**event.dict()).save()
    return {"message": "活动创建成功", "id": str(new_event.id)}

@router.get("/events")
async def get_events():
    events = await Event.objects().all()
    return [event.dict() for event in events]

@router.get("/event/{event_id}")
async def get_event(event_id: str):
    event = await Event.objects(event_id=event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="活动不存在")
    return event.dict()