from fastapi import APIRouter, HTTPException
from app.models.r2egulation_model import Regulation
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class RegulationCreate(BaseModel):
    regulation_id: str
    regulation_name: str
    regulation_content: str

@router.post("/regulation")
async def create_regulation(regulation: RegulationCreate):
    try:
        new_regulation = Regulation(**regulation.dict()).save()
        return {"message": "规章制度创建成功", "id": str(new_regulation.id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#这个得是去写一个鉴权，让3级用户登陆完才能看见
@router.get("/regulation/{regulation_id}")
async def get_regulation(regulation_id: str):
    regulation = Regulation.objects(id=regulation_id).first()
    if not regulation:
        raise HTTPException(status_code=404, detail="规章制度不存在")
    return regulation.to_dict()

@router.get("/regulations")
async def list_regulations():
    regulations = Regulation.objects()
    return [regulation.to_dict() for regulation in regulations]  # 修复了 to_dict() 的调用

@router.put("/regulation/{regulation_id}")  # 修复了URL路径拼写错误
async def update_regulation(regulation_id: str, regulation: RegulationCreate):
    existing_regulation = Regulation.objects(id=regulation_id).first()  # 重命名变量避免冲突
    if not existing_regulation:
        raise HTTPException(status_code=404, detail="规章制度不存在")
    existing_regulation.update(**regulation.dict())
    return {"message": "规章制度更新成功"}

@router.delete("/regulation/{regulation_id}")
async def delete_regulation(regulation_id: str):
    regulation = Regulation.objects(id=regulation_id).first()
    if not regulation:
        raise HTTPException(status_code=404, detail="规章制度不存在")
    regulation.delete()
    return {"message": "规章制度删除成功"}