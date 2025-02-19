from fastapi import APIRouter, HTTPException
from app.models.v8enue_borrow_model import VenueBorrow
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class VenueRequest(BaseModel):
    apply_id: str
    name: str
    student_id: str
    phonenum: str
    email: str
    purpose: str
    mentor_name: str
    mentor_phone_num: str
    picture: str
    start_time: datetime
    end_time: datetime

@router.post("/venue")
async def create_venue_request(request: VenueRequest):
    new_request = await VenueBorrow(**request.dict()).save()
    return {"message": "场地申请创建成功", "id": str(new_request.id)}

@router.put("/venue/{apply_id}")
async def update_venue_status(apply_id: str, state: int, reason: str = None):
    venue = await VenueBorrow.objects(apply_id=apply_id).first()
    if not venue:
        raise HTTPException(status_code=404, detail="场地申请不存在")
    venue.state = state
    venue.reason = reason
    await venue.save()
    return {"message": "场地申请状态更新成功"}