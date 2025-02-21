from fastapi import APIRouter, HTTPException
from app.models.s14chedule_model import Schedule
from pydantic import BaseModel

router = APIRouter()

class ScheduleCreate(BaseModel):
    name: str
    type: str
    order: int

@router.post("/schedule")
async def create_schedule(schedule: ScheduleCreate):
    new_schedule =  Schedule(**schedule.dict()).save()
    return {"message": "排班创建成功", "id": str(new_schedule.id)}

@router.get("/schedules")
async def get_schedules(type: str = None):
    query = {}
    if type:
        query["type"] = type
    schedules =  Schedule.objects(**query).all()
    return [schedule.dict() for schedule in schedules]