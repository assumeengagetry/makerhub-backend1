from fastapi import APIRouter, HTTPException
from app.models.s7tuff_model import Stuff
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class StuffCreate(BaseModel):
    stuff_id: str
    type: str
    stuff_name: str
    number: int
    description: Optional[str] = None

@router.post("/stuff")
async def create_stuff(stuff: StuffCreate):
    new_stuff = await Stuff(**stuff.dict()).save()
    return {"message": "物资创建成功", "id": str(new_stuff.id)}

@router.get("/stuff/{stuff_id}")
async def get_stuff(stuff_id: str):
    stuff = await Stuff.objects(stuff_id=stuff_id).first()
    if not stuff:
        raise HTTPException(status_code=404, detail="物资不存在")
    return stuff.dict()

@router.put("/stuff/{stuff_id}")
async def update_stuff(stuff_id: str, number: int):
    stuff = await Stuff.objects(stuff_id=stuff_id).first()
    if not stuff:
        raise HTTPException(status_code=404, detail="物资不存在")
    
    stuff.number = number
    await stuff.save()
    return {"message": "物资信息更新成功"}
