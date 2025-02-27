from fastapi import APIRouter, HTTPException, Depends
from app.models.d12uty_model import DutyRecord
from app.services.d12uty_service import DutyService
from app.core.auth import require_admin, AuthMiddleware
from datetime import datetime

router = APIRouter()
duty_service = DutyService()

@router.post("/duty/record", summary="创建值班记录")
async def create_duty_record(
    userid: str,
    name: str, 
    start_time: datetime, 
    end_time: datetime,
    current_user = Depends(AuthMiddleware.get_current_user)  # 允许所有登录用户
):
    total_hours = (end_time - start_time).total_seconds() / 3600
    record = DutyRecord(
        userid=userid,
        name=name,
        start_time=start_time,
        end_time=end_time,
        total=total_hours
    )
    result = await duty_service.create_duty_record(record)
    return {"message": "值班记录创建成功", "id": result["id"]}

@router.get("/duty/records", summary="获取所有值班记录")
async def get_duty_records(
    _=Depends(require_admin)  # 需要管理员权限
):
    return await duty_service.get_duty_records()