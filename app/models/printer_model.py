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