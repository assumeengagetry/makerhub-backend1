from datetime import datetime
from pydantic import BaseModel, Field

class CleaningBase(BaseModel):
    record_id: str
    name: str
    userid: str
    times: int

class CleaningCreate(CleaningBase):
    pass

class CleaningUpdate(BaseModel):
    times: int

class CleaningInDB(CleaningBase):
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True