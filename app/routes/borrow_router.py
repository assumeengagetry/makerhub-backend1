from fastapi import APIRouter, HTTPException
from app.models.stuff_borrow_model import StuffBorrow
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class BorrowRequest(BaseModel):
    sb_id: str
    userid: str
    name: str
    phone_num: str
    email: str
    grade: str
    major: str
    project_num: str
    type: str
    stuff_name: str
    stuff_quantity_change: int
    deadline: datetime
    reason: str
    categories: int

@router.post("/borrow")
async def create_borrow_request(request: BorrowRequest):
    new_request = await StuffBorrow(**request.dict(), state=0).save()
    return {"message": "借用申请创建成功", "id": str(new_request.id)}

@router.put("/borrow/{sb_id}")
async def update_borrow_status(sb_id: str, state: int):
    borrow = await StuffBorrow.objects(sb_id=sb_id).first()
    if not borrow:
        raise HTTPException(status_code=404, detail="借用申请不存在")
    borrow.state = state
    await borrow.save()
    return {"message": "借用申请状态更新成功"}

@router.get("/borrows/{userid}")
async def get_user_borrows(userid: str):
    borrows = await StuffBorrow.objects(userid=userid).all()
    return [borrow.dict() for borrow in borrows]