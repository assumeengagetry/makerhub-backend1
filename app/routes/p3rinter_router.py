from fastapi import APIRouter, HTTPException, Depends
from app.models.p3rinter_model import PrinterApplication
from typing import Optional, List
from pydantic import BaseModel
from app.core.auth import require_permission_level, require_super, AuthMiddleware

router = APIRouter()

class PrintCreate(BaseModel):
    phone_num: str
    name: str
    quantity: float
    printer: int
    file_zip: str

@router.post("/print/apply")
async def create_print_request(print_request: PrintCreate):
    new_print = PrinterApplication(**print_request.dict()).save()
    return {"code": 200,
            "status": "success",
            "message": "打印申请创建成功",
            "data" :{"apply_id": str(new_print.apply_id)}
            }

@router.get("/print/history/{apply_id}")
async def get_print_request(apply_id: str):
    print_req = PrinterApplication.objects(apply_id=apply_id).first()
    if not print_req:
        raise HTTPException(status_code=404, detail="打印申请不存在")
    return print_req.dict()

@router.put("/print/{apply_id}")
async def update_print_status(apply_id: str, state: int, reason: Optional[str] = None):
    print_req = PrinterApplication.objects(apply_id=apply_id).first()
    if not print_req:
        raise HTTPException(status_code=404, detail="打印申请不存在")
    
    print_req.state = state
    if reason:
        print_req.reason = reason
    print_req.save()
    return {"message": "打印申请状态更新成功"}


@router.get("/api/3d_print/history/{userid}")
async def get_user_history_printer(
    userid: str,
    user = Depends(AuthMiddleware.get_current_user)
):
    if user.level < 2:  # 检查超级管理员权限
        raise HTTPException(status_code=403, detail="权限不足")
    
    print_reqs = PrinterApplication.objects(userid=userid)
    records = []
    
    for req in print_reqs:
        records.append({
            "apply_id": req.apply_id,
            "quantity": req.quantity,
            "printer": req.printer,
            "score_change": req.score_change,
            "created_at": req.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "state": req.state,
            "reason": req.reason
        })
    
    return {
        "code": 200,
        "status": "success",
        "message": "获取历史申请成功",
        "data": {
            "records": records
        }
    }