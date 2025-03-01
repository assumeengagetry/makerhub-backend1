from mongoengine import Document, StringField, IntField, FloatField, DateTimeField
from .base_model import BaseModel

class PrinterApplication(BaseModel):
    apply_id = StringField(required=True, unique=True)
    userid = StringField(required=True)
    phone_num = StringField(required=True)
    score = IntField(default=0)
    score_change = IntField(default=0)
    name = StringField(required=True)
    quantity = FloatField(required=True)  # 用料量（克）
    printer = IntField(required=True)  # 0: i创街，1: 208
    file_zip = StringField()  # Base64编码的ZIP文件
    state = IntField(default=0)  # 0: 未审核，1: 审核通过，2: 审核未通过
    reason = StringField()

    meta = {
        'collection': 'printer_applications',
        'indexes': ['apply_id', 'userid']
    }
    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "apply_id": self.apply_id,
            "userid": self.userid,
            "phone_num": self.phone_num,
            "score": self.score,
            "score_change": self.score_change,
            "name": self.name,
            "quantity": self.quantity,
            "printer": self.printer,
            "file_zip": self.file_zip,
            "state": self.state,
            "reason": self.reason,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
