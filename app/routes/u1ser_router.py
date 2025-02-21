# filepath: /society-management/society-management/app/routes/user_router.py

from fastapi import APIRouter, HTTPException
from app.models.u1ser_model import User
from typing import Optional
from pydantic import BaseModel
from passlib.hash import bcrypt

router = APIRouter()

class UserCreate(BaseModel):
    userid: str
    password: str
    real_name: str
    phone_num: str
    level: Optional[int] = 1

@router.post("/register")
async def register(user: UserCreate):
    if  User.objects(userid=user.userid).first():
        raise HTTPException(status_code=400, detail="用户已存在")
    
    hashed_password = bcrypt.hash(user.password)
    new_user =  User(
        userid=user.userid,
        password=hashed_password,
        real_name=user.real_name,
        phone_num=user.phone_num,
        level=user.level
    ).save()
    return {"message": "注册成功", "id": str(new_user.id)}

@router.post("/login")
async def login(userid: str, password: str):
    user =  User.objects(userid=userid).first()
    if not user or not bcrypt.verify(password, user.password):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    
    return {
        "message": "登录成功",
        "user": {
            "userid": user.userid,
            "real_name": user.real_name,
            "level": user.level
        }
    }