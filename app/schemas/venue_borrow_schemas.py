# 文件：/society-management/society-management/app/schemas/venue_borrow_schemas.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class VenueBorrowBase(BaseModel):
    apply_id: str
    name: str
    student_id: str
    phonenum: str
    email: str
    purpose: str
    mentor_name: str
    mentor_phone_num: str
    picture: Optional[str]  # base64编码的场地平面图
    start_time: datetime
    end_time: datetime
    state: int = 0  # 0: 待审核，1: 审核通过，2: 审核未通过
    reason: Optional[str] = None

class VenueBorrowCreate(VenueBorrowBase):
    pass

class VenueBorrowUpdate(BaseModel):
    state: Optional[int] = None
    reason: Optional[str] = None

class VenueBorrowInDB(VenueBorrowBase):
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True