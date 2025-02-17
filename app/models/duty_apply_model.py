from sqlalchemy import Column, String, Integer, Date
from .base_model import BaseModel

class DutyApply(BaseModel):
    __tablename__ = 'duty_applies'

    apply_id = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    userid = Column(String(100), nullable=False)
    day = Column(Date, nullable=False)
    time_section = Column(Integer, nullable=False)  # 1-6