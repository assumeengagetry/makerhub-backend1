from fastapi import APIRouter, HTTPException, Depends
from app.models.e4vent_model import Event
from app.services.e4vent_service import EventService
from app.core.auth import require_admin, AuthMiddleware
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

router = APIRouter()
event_service = EventService()

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

@router.post("/events/post", summary="创建活动")
async def create_event(
    event: EventCreate,
    _=Depends(require_admin)  # 需要管理员权限
):
    result = await event_service.create_event(Event(**event.dict()))
    return {"code": 200, "id": result["id"]}

@router.get("/events/view", summary="获取活动列表")
async def list_events(
    current_user = Depends(AuthMiddleware.get_current_user)  # 允许所有登录用户访问
):
    return await event_service.list_events()

@router.get("/event/details/{event_id}", summary="获取活动详情")
async def get_event(
    event_id: str,
    current_user = Depends(AuthMiddleware.get_current_user)  # 允许所有登录用户访问
):
    event = await event_service.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="活动不存在")
    return event