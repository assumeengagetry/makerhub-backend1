from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class PrinterRequestBase(BaseModel):
    apply_id: str
    userid: str
    phone_num: str
    score: int
    score_change: int
    name: str
    quantity: float
    printer: int  # 0: i创街，1: 208
    file_zip: str
    state: int = 0  # 0: 未审核，1: 审核通过，2: 审核未通过
    reason: Optional[str] = None

class PrinterRequestCreate(PrinterRequestBase):
    pass

class PrinterRequestUpdate(BaseModel):
    state: Optional[int] = None
    reason: Optional[str] = None
    score_change: Optional[int] = None

class PrinterRequestInDB(PrinterRequestBase):
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True