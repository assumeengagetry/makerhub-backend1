from fastapi import APIRouter, HTTPException
from app.models.s14chedule_model import Arrange
from pydantic import BaseModel

router = APIRouter()

class ScheduleCreate(BaseModel):
    name: str
    type: str
    order: int

@router.post("/schedule")
async def create_schedule(schedule: ScheduleCreate):
    new_schedule = await Arrange(**schedule.dict()).save()
    return {"message": "排班创建成功", "id": str(new_schedule.id)}

@router.get("/schedules")
async def get_schedules(type: str = None):
    query = {}
    if type:
        query["type"] = type
    schedules = await Arrange.objects(**query).all()
    return [schedule.dict() for schedule in schedules]