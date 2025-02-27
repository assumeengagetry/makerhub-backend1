from typing import Optional
from pydantic import BaseModel, Field

class RegulationBase(BaseModel):
    file_id: str
    file_name: str
    content: str

class RegulationInDB(RegulationBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True