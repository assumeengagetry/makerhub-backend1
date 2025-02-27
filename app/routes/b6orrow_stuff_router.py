from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.b6orrow_stuff_model import BorrowRecord
from app.services.b6orrow_stuff_service import BorrowService
from app.core.auth import require_admin, AuthMiddleware
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()
borrow_service = BorrowService()

class BorrowRequest(BaseModel):
    """借用申请请求模型"""
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

@router.post("/borrow", summary="创建借用申请")
async def create_borrow_request(
    request: BorrowRequest,
    current_user = Depends(AuthMiddleware.get_current_user)
):
    borrow_record = BorrowRecord(**request.dict())
    result = await borrow_service.create_borrow(borrow_record)
    return {"message": "借用申请创建成功", "id": result["id"]}

@router.put("/borrow/{borrow_id}", summary="更新借用状态")
async def update_borrow_status(
    borrow_id: str, 
    state: int,
    _=Depends(require_admin)
):
    result = await borrow_service.update_borrow_status(borrow_id, state)
    if not result:
        raise HTTPException(status_code=404, detail="借用申请不存在")
    return {"message": "借用状态更新成功"}

@router.get("/borrows/user", summary="获取用户借用记录")
async def get_user_borrows(
    current_user = Depends(AuthMiddleware.get_current_user)
) -> List[dict]:
    filters = {"userid": current_user.userid}
    return await borrow_service.get_borrows(filters)

@router.get("/borrows", summary="获取所有借用记录")
async def get_all_borrows(
    _=Depends(require_admin)
) -> List[dict]:
    return await borrow_service.get_borrows()