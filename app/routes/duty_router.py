from fastapi import APIRouter, HTTPException
from app.models.duty_apply_model import DutyApply
from app.models.duty_record_model import DutyRecord
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
    new_request = await DutyApply(**request.dict()).save()
    return {"message": "值班申请创建成功", "id": str(new_request.id)}

@router.post("/duty/record")
async def create_duty_record(userid: str, name: str, start_time: datetime, end_time: datetime):
    total_hours = (end_time - start_time).total_seconds() / 3600
    new_record = await DutyRecord(
        userid=userid,
        name=name,
        start_time=start_time,
        end_time=end_time,
        total=total_hours
    ).save()
    return {"message": "值班记录创建成功", "id": str(new_record.id)}