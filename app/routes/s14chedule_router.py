from fastapi import APIRouter, HTTPException, Depends
from app.models.s14chedule_model import Schedule
from app.services.s14chedule_service import ScheduleService
from app.core.auth import AuthMiddleware, require_admin
from pydantic import BaseModel

router = APIRouter()
schedule_service = ScheduleService()

class ScheduleCreate(BaseModel):
    name: str
    type: str
    order: int

@router.post("/schedule", summary="创建排班")
async def create_schedule(
    schedule: ScheduleCreate,
    current_user = Depends(require_admin)  # 只允许管理员创建排班
):
    result = await schedule_service.create_schedule(Schedule(**schedule.dict()))
    return {"message": "排班创建成功", "id": result["id"]}

@router.get("/schedule/{schedule_id}", summary="获取排班详情")
async def get_schedule(
    schedule_id: str,
    current_user = Depends(require_admin)  # 不允许最低等级用户获取排班
):
    schedule = await schedule_service.get_schedule(schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="排班不存在")
    return schedule