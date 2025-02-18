from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import get_database
from app.models.t5ask_model import TaskModel

class TaskService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.tasks

    async def create_task(self, task: TaskModel) -> dict:
        task_dict = task.dict(exclude_unset=True)
        task_dict.update({
            "created_at": datetime.utcnow(),
            "state": 0  # 未完成状态
        })
        result = await self.collection.insert_one(task_dict)
        return {"id": str(result.inserted_id)}

    async def update_task_status(self, task_id: str, state: int) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"state": state}}
        )
        return result.modified_count > 0

    async def get_tasks(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        tasks = []
        cursor = self.collection.find(query).sort("deadline", 1)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            tasks.append(doc)
        return tasks