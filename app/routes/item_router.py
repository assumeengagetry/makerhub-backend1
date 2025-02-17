from fastapi import APIRouter, HTTPException
from app.models.stuff_model import Stuff
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class ItemCreate(BaseModel):
    stuff_id: str
    type: str
    name: str
    quantity: int
    description: Optional[str] = None

@router.post("/item")
async def create_item(item: ItemCreate):
    new_item = await Stuff(
        stuff_id=item.stuff_id,
        type=item.type,
        stuff_name=item.name,
        number=item.quantity,
        description=item.description
    ).save()
    return {"message": "物品创建成功", "id": str(new_item.id)}

@router.get("/items")
async def get_items(type: str = None):
    query = {}
    if type:
        query["type"] = type
    items = await Stuff.objects(**query).all()
    return [item.dict() for item in items]

@router.delete("/item/{stuff_id}")
async def delete_item(stuff_id: str):
    item = await Stuff.objects(stuff_id=stuff_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="物品不存在")
    await item.delete()
    return {"message": "物品删除成功"}