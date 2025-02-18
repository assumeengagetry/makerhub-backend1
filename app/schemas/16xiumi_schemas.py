# 文件：/society-management/society-management/app/schemas/xiumi_schemas.py

from pydantic import BaseModel, Field

class XiumiBase(BaseModel):
    name: str  # 提交人姓名
    userid: str  # 提交人邮箱
    link: str  # 秀米链接

class XiumiCreate(XiumiBase):
    pass

class XiumiUpdate(BaseModel):
    link: str

class XiumiInDB(XiumiBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True