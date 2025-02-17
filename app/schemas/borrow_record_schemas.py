from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class BorrowRecordBase(BaseModel):
    sb_id: str
    userid: str
    name: str
    phone_num: str
    email: str
    grade: str
    major: str
    project_num: Optional[str]
    type: str
    stuff_name: str
    stuff_quantity_change: int
    deadline: datetime
    reason: str
    categories: int  # 0个人，1团队
    state: int = 0  # 0未审核，1已审核

class BorrowRecordCreate(BorrowRecordBase):
    pass

class BorrowRecordUpdate(BaseModel):
    state: int
    deadline: Optional[datetime] = None
    stuff_quantity_change: Optional[int] = None

class BorrowRecordInDB(BorrowRecordBase):
    id: str = Field(..., alias="_id")
    created_at: datetime

    class Config:
        allow_population_by_field_name = True