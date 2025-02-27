from mongoengine import Document, StringField, IntField, DateTimeField
from .base_model import BaseModel

class BorrowRecord(BaseModel):
    """借用记录模型"""
    
    meta = {
        'collection': 'borrow_records',
        'indexes': ['sb_id', 'userid']
    }
    
    # 基本信息
    sb_id = StringField(required=True, unique=True)
    userid = StringField(required=True)
    name = StringField(required=True)
    phone_num = StringField()
    email = StringField()
    
    # 学籍信息
    grade = StringField()
    major = StringField()
    project_num = StringField()
    
    # 借用信息
    type = StringField()
    stuff_name = StringField()
    stuff_quantity_change = IntField()
    deadline = DateTimeField()
    reason = StringField()
    
    # 状态信息
    categories = IntField()  # 0: 个人, 1: 团队
    state = IntField(default=0)  # 0: 未审核, 1: 已审核

