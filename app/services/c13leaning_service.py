from typing import List
from loguru import logger
from app.models.c13leaning_model import CleaningRecord

class CleaningService:
    async def create_cleaning_record(self, record_data: dict) -> dict:
        try:
            record = CleaningRecord(**record_data)
            record.save()
            logger.info(f"创建清洁记录成功: {record.id}")
            return {"id": str(record.id)}
        except Exception as e:
            logger.error(f"创建清洁记录失败: {e}")
            raise

    async def get_cleaning_records(self, user_id: str = None) -> List[dict]:
        query = {"userid": user_id} if user_id else {}
        records = CleaningRecord.objects(**query)
        return [record.to_dict() for record in records]

    async def update_cleaning_times(self, record_id: str, times: int) -> bool:
        try:
            record = CleaningRecord.objects.get(id=record_id)
            record.times = times
            record.save()
            return True
        except CleaningRecord.DoesNotExist:
            return False