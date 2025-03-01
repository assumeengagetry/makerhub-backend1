from mongoengine import Document, DateTimeField
from datetime import datetime

class BaseModel(Document):
    meta = {'abstract': True}
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)
    def to_dict(self):
        """转换为字典格式"""
        return {field: getattr(self, field) for field in self._fields}