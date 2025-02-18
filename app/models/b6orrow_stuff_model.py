from mongoengine import Document, StringField, IntField, DateTimeField
from .base_model import BaseModel

class BorrowRecord(BaseModel):
    meta = {'collection': 'borrow_records'}
    
    sb_id = StringField(required=True, unique=True)
    userid = StringField(required=True)
    name = StringField(required=True)
    phone_num = StringField()
    email = StringField()
    grade = StringField()
    major = StringField()
    project_num = StringField()
    type = StringField()
    stuff_name = StringField()
    stuff_quantity_change = IntField()
    deadline = DateTimeField()
    reason = StringField()
    categories = IntField()  # 0: 个人, 1: 团队
    state = IntField(default=0)  # 0: 未审核, 1: 已审核