from fastapi import APIRouter, HTTPException
from app.models.print_model import Print
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class PrintCreate(BaseModel):
    apply_id: str
    userid: str
    phone_num: str
    name: str
    quantity: float
    printer: int
    file_zip: str

@router.post("/print")
async def create_print_request(print_request: PrintCreate):
    new_print = await Print(**print_request.dict()).save()
    return {"message": "打印申请创建成功", "id": str(new_print.id)}

@router.get("/print/{apply_id}")
async def get_print_request(apply_id: str):
    print_req = await Print.objects(apply_id=apply_id).first()
    if not print_req:
        raise HTTPException(status_code=404, detail="打印申请不存在")
    return print_req.dict()

@router.put("/print/{apply_id}")
async def update_print_status(apply_id: str, state: int, reason: Optional[str] = None):
    print_req = await Print.objects(apply_id=apply_id).first()
    if not print_req:
        raise HTTPException(status_code=404, detail="打印申请不存在")
    
    print_req.state = state
    if reason:
        print_req.reason = reason
    await print_req.save()
    return {"message": "打印申请状态更新成功"}