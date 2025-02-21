from fastapi import APIRouter, HTTPException
from app.models.d12uty_model import DutyRecord
from datetime import datetime

router = APIRouter()

@router.post("/duty/record")
async def create_duty_record(userid: str, name: str, start_time: datetime, end_time: datetime):
    total_hours = (end_time - start_time).total_seconds() / 3600
    new_record =  DutyRecord(
        userid=userid,
        name=name,
        start_time=start_time,
        end_time=end_time,
        total=total_hours
    ).save()
    return {"message": "值班记录创建成功", "id": str(new_record.id)}