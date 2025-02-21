from fastapi import APIRouter, HTTPException
from app.models.d11uty_apply_model import DutyApply
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class DutyRequest(BaseModel):
    apply_id: str
    name: str
    userid: str
    day: datetime
    time_section: int

@router.post("/duty/apply")
async def create_duty_request(request: DutyRequest):
    new_request =  DutyApply(**request.dict()).save()
    return {"message": "值班申请创建成功", "id": str(new_request.id)}
