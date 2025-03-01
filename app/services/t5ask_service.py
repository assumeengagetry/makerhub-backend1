from typing import List
from app.models.t5ask_model import Task

class TaskService:
    async def create_task(self, task_data: dict) -> dict:
        task = Task(**task_data)
        task.state = 0  # 未完成状态
        task.save()
        return {"id": str(task.id)}

    async def update_task_status(self, task_id: str, state: int) -> bool:
        try:
            task = Task.objects.get(id=task_id)
            task.state = state
            task.save()
            return True
        except Task.DoesNotExist:
            return False

    async def get_tasks(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        tasks = Task.objects(**query).order_by("+deadline")
        return [task.to_dict() for task in tasks]