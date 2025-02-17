# 文件：/society-management/society-management/app/schemas/duty_record_schemas.py

from datetime import datetime
from pydantic import BaseModel, Field

class DutyRecordBase(BaseModel):
    name: str
    userid: str
    start_time: datetime
    end_time: datetime
    total: float  # 值班时长(小时)

class DutyRecordCreate(DutyRecordBase):
    pass

class DutyRecordUpdate(BaseModel):
    end_time: datetime
    total: float

class DutyRecordInDB(DutyRecordBase):
    id: str = Field(..., alias="_id")
    created_at: datetime

    class Config:
        allow_population_by_field_name = True