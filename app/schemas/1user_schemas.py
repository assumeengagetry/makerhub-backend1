from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    userid: EmailStr  # 用户邮箱
    level: int = 1  # 1：會員，2：干事，3：部长及以上
    real_name: str
    phone_num: str
    note: Optional[str] = None # 自我介紹
    state: int = 1  # 0：封禁，1：正常
    profile_photo: Optional[str] = None  # base64编码的头像
    score: int = 0

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    level: Optional[int] = None
    real_name: Optional[str] = None
    phone_num: Optional[str] = None
    note: Optional[str] = None
    state: Optional[int] = None
    profile_photo: Optional[str] = None
    score: Optional[int] = None
    
class UserInDB(UserBase):
    id: str = Field(..., alias="_id")
    password: str  # 存储加密后的密码

    class Config:
        allow_population_by_field_name = True