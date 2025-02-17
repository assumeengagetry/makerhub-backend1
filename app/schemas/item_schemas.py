from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    stuff_id: str
    type: str
    stuff_name: str
    number: int
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    type: Optional[str] = None
    stuff_name: Optional[str] = None
    number: Optional[int] = None
    description: Optional[str] = None

class ItemInDB(ItemBase):
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True