from fastapi import APIRouter, HTTPException, Depends
from app.models.r2egulation_model import Regulation
from app.services.r2egulation_service import RegulationService
from app.core.auth import AuthMiddleware
from typing import Optional
from pydantic import BaseModel

router = APIRouter()
regulation_service = RegulationService()

class RegulationCreate(BaseModel):
    regulation_id: str
    regulation_name: str
    regulation_content: str

@router.get("/regulation/get/{regulation_id}", summary="获取规章制度")
async def get_regulation(
    regulation_id: str,
    current_user = Depends(AuthMiddleware.get_current_user)  # 允许所有登录用户访问
):
    regulation = await regulation_service.get_regulation(regulation_id)
    if not regulation:
        raise HTTPException(status_code=404, detail="规章制度不存在")
    return regulation
