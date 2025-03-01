from typing import List, Optional
from loguru import logger
from app.models.e4vent_model import Event

class EventService:
    async def create_event(self, event_data: dict) -> dict:
        try:
            event = Event(**event_data)
            event.save()
            logger.info(f"活动创建成功: {event.id}")
            return {"id": str(event.id)}
        except Exception as e:
            logger.error(f"创建活动失败: {e}")
            raise

    async def get_event(self, event_id: str) -> Optional[dict]:
        try:
            event = Event.objects.get(id=event_id)
            return event.to_dict()
        except Event.DoesNotExist:
            return None

    async def list_events(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        events = Event.objects(**query).order_by("+start_time")
        return [event.to_dict() for event in events]