from fastapi import APIRouter, HTTPException
from app.models.r2egulation_model import Regulation
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class RegulationCreate(BaseModel):
    regulation_id: str
    regulation_name: str
    regulation_content: str


@router.get("/regulation/{regulation_id}")
async def get_regulation(regulation_id: str):
    regulation = Regulation.objects(id=regulation_id).first()
    if not regulation:
        raise HTTPException(status_code=404, detail="规章制度不存在")
    return regulation.to_dict()
