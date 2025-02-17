from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class ProjectBase(BaseModel):
    apply_id: str
    project_name: str
    director: str
    college: str
    major_grade: str
    phone_num: str
    email: str
    mentor: str
    description: str
    application_file: Optional[str]
    prove_file: Optional[str]
    member: List[str]
    start_time: datetime
    end_time: datetime
    audit_state: int = 0  # 0：待审核，1：通过，2：拒绝
    project_state: int = 1  # 0：已结束，1：进行中

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    director: Optional[str] = None
    description: Optional[str] = None
    audit_state: Optional[int] = None
    project_state: Optional[int] = None

class ProjectInDB(ProjectBase):
    id: str = Field(..., alias="_id")
    created_at: datetime

    class Config:
        allow_population_by_field_name = True