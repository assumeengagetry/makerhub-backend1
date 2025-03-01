from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    task_id: str
    department: str
    task_name: str
    name: str
    content: str
    state: int = 0  # 0: 未完成，1: 已完成
    deadline: datetime

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    task_name: Optional[str] = None
    content: Optional[str] = None
    state: Optional[int] = None
    deadline: Optional[datetime] = None

class TaskInDB(TaskBase):
    id: str = Field(..., alias="_id")
    created_at: datetime

    class Config:
        allow_population_by_field_name = True