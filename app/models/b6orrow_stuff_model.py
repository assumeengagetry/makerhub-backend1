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

    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "sb_id": self.sb_id,
            "userid": self.userid,
            "name": self.name,
            "phone_num": self.phone_num,
            "email": self.email,
            "grade": self.grade,
            "major": self.major,
            "project_num": self.project_num,
            "type": self.type,
            "stuff_name": self.stuff_name,
            "stuff_quantity_change": self.stuff_quantity_change,
            "deadline": self.deadline,
            "reason": self.reason,
            "categories": self.categories,
            "state": self.state,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

