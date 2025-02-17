from pydantic import BaseModel, Field

class ScheduleBase(BaseModel):
    name: str
    type: str  # 工作类型（如活动文案、公众号等）
    order: int

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleUpdate(BaseModel):
    type: str
    order: int

class ScheduleInDB(ScheduleBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True