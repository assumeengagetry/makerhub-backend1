from datetime import datetime, date
from pydantic import BaseModel, Field

class DutyApplyBase(BaseModel):
    apply_id: str
    name: str
    userid: str
    day: date
    time_section: int  # 1-6时段

class DutyApplyCreate(DutyApplyBase):
    pass

class DutyApplyUpdate(BaseModel):
    time_section: int

class DutyApplyInDB(DutyApplyBase):
    id: str = Field(..., alias="_id")
    created_at: datetime

    class Config:
        allow_population_by_field_name = True