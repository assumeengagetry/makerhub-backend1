from fastapi import APIRouter, HTTPException
from app.models.c13leaning_model import CleaningRecord
from pydantic import BaseModel

router = APIRouter()

class CleaningRecord(BaseModel):
    record_id: str
    name: str
    userid: str
    times: int = 1

@router.post("/cleaning")
async def create_cleaning_record(record: CleaningRecord):
    new_record =  CleaningRecord(**record.dict()).save()
    return {"message": "清洁记录创建成功", "id": str(new_record.id)}

@router.get("/cleaning/{userid}")
async def get_cleaning_records(userid: str):
    records =  CleaningRecord.objects(userid=userid).all()
    return [record.dict() for record in records]