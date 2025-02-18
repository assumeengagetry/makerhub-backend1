from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class CompetitionBase(BaseModel):
    game_id: str
    name: str
    wx_num: Optional[str]
    qq_num: Optional[str]
    introduction: str
    registration_start: datetime
    registration_end: datetime
    contest_start: datetime
    contest_end: datetime
    link: str

class CompetitionCreate(CompetitionBase):
    pass

class CompetitionUpdate(BaseModel):
    name: Optional[str] = None
    introduction: Optional[str] = None
    link: Optional[str] = None

class CompetitionInDB(CompetitionBase):
    id: str = Field(..., alias="_id")
    created_at: datetime

    class Config:
        allow_population_by_field_name = True