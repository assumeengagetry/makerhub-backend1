from typing import List, Optional
from app.models.s14chedule_model import Schedule

class ScheduleService:
    async def create_schedule(self, schedule_data: dict) -> dict:
        schedule = Schedule(**schedule_data)
        schedule.save()
        return {"id": str(schedule.id)}

    async def update_schedule(self, schedule_id: str, data: dict) -> bool:
        try:
            schedule = Schedule.objects.get(id=schedule_id)
            for key, value in data.items():
                setattr(schedule, key, value)
            schedule.save()
            return True
        except Schedule.DoesNotExist:
            return False

    async def get_schedules(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        schedules = Schedule.objects(**query).order_by("+order")
        return [schedule.to_dict() for schedule in schedules]

    async def get_schedule(self, schedule_id: str) -> Optional[dict]:
        try:
            schedule = Schedule.objects.get(id=schedule_id)
            return schedule.to_dict()
        except Schedule.DoesNotExist:
            return None