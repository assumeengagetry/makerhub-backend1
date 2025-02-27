from fastapi import APIRouter, HTTPException, Depends
from app.models.v8enue_borrow_model import VenueBorrow
from app.services.v8enue_borrow_service import VenueService
from app.core.auth import AuthMiddleware, require_admin
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()
venue_service = VenueService()

class VenueRequest(BaseModel):
    apply_id: str
    name: str
    student_id: str
    phonenum: str
    email: str
    purpose: str
    mentor_name: str
    mentor_phone_num: str
    picture: str
    start_time: datetime
    end_time: datetime

@router.post("/venue", summary="创建场地申请")
async def create_venue_request(
    request: VenueRequest,
    current_user = Depends(AuthMiddleware.get_current_user)  # 允许所有登录用户申请
):
    result = await venue_service.create_venue_request(VenueBorrow(**request.dict()))
    return {"message": "场地申请创建成功", "id": result["id"]}

@router.put("/venue/{apply_id}", summary="更新场地申请状态")
async def update_venue_status(
    apply_id: str,
    state: int,
    reason: str = None,
    current_user = Depends(require_admin)  # 需要管理员权限
):
    success = await venue_service.update_venue_status(apply_id, state, reason)
    if not success:
        raise HTTPException(status_code=404, detail="场地申请不存在")
    return {"message": "场地申请状态更新成功"}

@router.get("/venue/{apply_id}", summary="获取场地申请详情")
async def get_venue_request(
    apply_id: str,
    current_user = Depends(require_admin)  # 需要管理员权限
):
    venue = await venue_service.get_venue_request(apply_id)
    if not venue:
        raise HTTPException(status_code=404, detail="场地申请不存在")
    return venue