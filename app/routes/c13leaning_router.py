from fastapi import APIRouter, HTTPException, Depends
from app.models.c13leaning_model import CleaningRecord
from app.services.c13leaning_service import CleaningService
from app.core.auth import require_admin, AuthMiddleware
from pydantic import BaseModel

router = APIRouter()
cleaning_service = CleaningService()

class CleaningRecordCreate(BaseModel):
    record_id: str
    name: str
    userid: str
    times: int = 1

@router.post("/cleaning", summary="创建清洁记录")
async def create_cleaning_record(
    record: CleaningRecordCreate,
    _=Depends(require_admin)  # 需要管理员权限
):
    result = await cleaning_service.create_cleaning_record(CleaningRecord(**record.dict()))
    return {"message": "清洁记录创建成功", "id": result["id"]}

@router.get("/cleaning", summary="获取所有清洁记录")
async def get_cleaning_records(
    _=Depends(require_admin)  # 需要管理员权限
):
    records = await cleaning_service.get_cleaning_records()
    return records