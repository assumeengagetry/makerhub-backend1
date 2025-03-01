from typing import List
from datetime import datetime
from loguru import logger
from app.models.d11uty_apply_model import DutyApply
from app.models.d12uty_model import DutyRecord

class DutyService:
    async def create_duty_apply(self, apply_data: dict) -> dict:
        apply = DutyApply(**apply_data)
        apply.save()
        return {"id": str(apply.id)}

    async def create_duty_record(self, record_data: dict) -> dict:
        try:
            record = DutyRecord(**record_data)
            record.save()
            logger.info(f"值班记录创建成功: {record.id}")
            return {"id": str(record.id)}
        except Exception as e:
            logger.error(f"创建值班记录失败: {e}")
            raise

    async def get_duty_applies(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        applies = DutyApply.objects(**query)
        return [apply.to_dict() for apply in applies]

    async def get_duty_records(self, user_id: str = None) -> List[dict]:
        query = {"userid": user_id} if user_id else {}
        records = DutyRecord.objects(**query)
        return [record.to_dict() for record in records]

    async def update_duty_record(self, record_id: str, data: dict) -> bool:
        try:
            record = DutyRecord.objects.get(id=record_id)
            for key, value in data.items():
                setattr(record, key, value)
            record.save()
            return True
        except DutyRecord.DoesNotExist:
            return False

    async def delete_duty_apply(self, apply_id: str) -> bool:
        try:
            apply = DutyApply.objects.get(id=apply_id)
            apply.delete()
            return True
        except DutyApply.DoesNotExist:
            return False