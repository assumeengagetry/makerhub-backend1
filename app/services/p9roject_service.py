from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongodb
from app.models.p9roject_model import Project

class ProjectService:
    def __init__(self):
        self.db = mongodb()
        self.collection = self.db.projects

    async def create_project(self, project: Project) -> dict:
        project_dict = project.dict(exclude_unset=True)
        project_dict["created_at"] = datetime.utcnow()
        project_dict["audit_state"] = 0  # 待审核状态
        project_dict["project_state"] = 1  # 进行中状态
        
        result = await self.collection.insert_one(project_dict)
        return {"id": str(result.inserted_id)}

    async def get_project(self, project_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(project_id):
            return None
        return await self.collection.find_one({"_id": ObjectId(project_id)})

    async def list_projects(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        projects = []
        cursor = self.collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            projects.append(doc)
        return projects

    async def update_project_status(self, project_id: str, audit_state: int) -> bool:
        if not ObjectId.is_valid(project_id):
            return False
        result = await self.collection.update_one(
            {"_id": ObjectId(project_id)},
            {"$set": {"audit_state": audit_state}}
        )
        return result.modified_count > 0

    async def complete_project(self, project_id: str) -> bool:
        if not ObjectId.is_valid(project_id):
            return False
        result = await self.collection.update_one(
            {"_id": ObjectId(project_id)},
            {"$set": {"project_state": 0}}
        )
        return result.modified_count > 0

    async def delete_project(self, project_id: str) -> bool:
        if not ObjectId.is_valid(project_id):
            return False
        result = await self.collection.delete_one({"_id": ObjectId(project_id)})
        return result.deleted_count > 0