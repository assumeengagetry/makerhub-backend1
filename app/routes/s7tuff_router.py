from fastapi import APIRouter, HTTPException, Depends
from app.models.s7tuff_model import Stuff
from app.services.s7tuff_service import StuffService
from app.core.auth import require_admin, AuthMiddleware
from typing import Optional
from pydantic import BaseModel

router = APIRouter()
stuff_service = StuffService()

class StuffCreate(BaseModel):
    stuff_id: str
    type: str
    stuff_name: str
    number: int
    description: Optional[str] = None

@router.post("/stuff", summary="创建物资")
async def create_stuff(
    stuff: StuffCreate,
    current_user = Depends(require_admin)  # 需要管理员权限
):
    result = await stuff_service.add_item(Stuff(**stuff.dict()))
    return {"message": "物资创建成功", "id": result["id"]}

@router.put("/stuff/{stuff_id}", summary="更新物资数量")
async def update_stuff(
    stuff_id: str,
    number: int,
    current_user = Depends(require_admin)  # 需要管理员权限
):
    success = await stuff_service.update_item_quantity(stuff_id, number)
    if not success:
        raise HTTPException(status_code=404, detail="物资不存在")
    return {"message": "物资信息更新成功"}

@router.get("/stuff/list", summary="获取物资列表")
async def get_stuff_list(
    current_user = Depends(AuthMiddleware.get_current_user)  # 允许所有登录用户访问
):
    return await stuff_service.get_item_list()
