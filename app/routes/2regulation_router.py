from fastapi import APIRouter, HTTPException
from app.models.r2egulation_model import Regulation
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class RegulationCreate(BaseModel):
    title: str
    content: str
    publisher: str

@router.post("/regulation")
async def create_regulation(regulation: RegulationCreate):
    try:
        new_regulation = Regulation(**regulation.dict()).save()
        return {"message": "规章制度创建成功", "id": str(new_regulation.id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/regulations")
async def get_regulations():
    regulations = Regulation.objects()
    return [regulation.to_dict() for regulation in regulations]

@router.get("/regulation/{regulation_id}")
async def get_regulation(regulation_id: str):
    regulation = Regulation.objects(id=regulation_id).first()
    if not regulation:
        raise HTTPException(status_code=404, detail="规章制度不存在")
    return regulation.to_dict()

@router.delete("/regulation/{regulation_id}")
async def delete_regulation(regulation_id: str):
    regulation = Regulation.objects(id=regulation_id).first()
    if not regulation:
        raise HTTPException(status_code=404, detail="规章制度不存在")
    regulation.delete()
    return {"message": "规章制度删除成功"}