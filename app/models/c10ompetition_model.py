from mongoengine import Document, StringField, DateTimeField
from .base_model import BaseModel

class Competition(BaseModel):
    meta = {
        'collection': 'competitions',
        'indexes': [
            'competition_id',
            'created_at'
        ]
    }
    
    competition_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    wx_num = StringField()
    qq_num = StringField()
    introduction = StringField()
    registration_start = DateTimeField()
    registration_end = DateTimeField()
    contest_start = DateTimeField()
    contest_end = DateTimeField()
    link = StringField()

    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "competition_id": self.competition_id,
            "name": self.name,
            "wx_num": self.wx_num,
            "qq_num": self.qq_num,
            "introduction": self.introduction,
            "registration_start": self.registration_start,
            "registration_end": self.registration_end,
            "contest_start": self.contest_start,
            "contest_end": self.contest_end,
            "link": self.link,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }