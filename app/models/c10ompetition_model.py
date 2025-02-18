from mongoengine import Document, StringField, DateTimeField
from .base_model import BaseModel

class Competition(BaseModel):
    meta = {'collection': 'competitions'}
    
    game_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    wx_num = StringField()
    qq_num = StringField()
    introduction = StringField()
    registration_start = DateTimeField()
    registration_end = DateTimeField()
    contest_start = DateTimeField()
    contest_end = DateTimeField()
    link = StringField()