from fastapi import APIRouter, HTTPException, Depends
from app.models.d11uty_apply_model import DutyApply
from app.services.d12uty_service import DutyService
from app.core.auth import require_admin, AuthMiddleware
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()
duty_service = DutyService()

class DutyRequest(BaseModel):
    apply_id: str
    name: str
    userid: str
    day: datetime
    time_section: int

@router.post("/duty/apply", summary="创建值班申请")
async def create_duty_request(
    request: DutyRequest,
    _=Depends(require_admin)  # 需要管理员权限
):
    result = await duty_service.create_duty_apply(DutyApply(**request.dict()))
    return {"message": "值班申请创建成功", "id": result["id"]}

@router.get("/duty/apply", summary="获取所有值班申请")
async def get_duty_requests(
    _=Depends(require_admin)  # 需要管理员权限
):
    return await duty_service.get_duty_applies()

@router.delete("/duty/apply/{apply_id}", summary="删除值班申请")
async def delete_duty_request(
    apply_id: str,
    _=Depends(require_admin)  # 需要管理员权限
):
    result = await duty_service.delete_duty_apply(apply_id)
    if not result:
        raise HTTPException(status_code=404, detail="值班申请不存在")
    return {"message": "值班申请删除成功"}