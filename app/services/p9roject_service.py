from typing import List, Optional
from app.models.p9roject_model import Project

class ProjectService:
    async def create_project(self, project_data: dict) -> dict:
        project = Project(**project_data)
        project.audit_state = 0  # 待审核状态
        project.project_state = 1  # 进行中状态
        project.save()
        return {"id": str(project.id)}

    async def get_project(self, project_id: str) -> Optional[dict]:
        try:
            project = Project.objects.get(id=project_id)
            return project.to_dict()
        except Project.DoesNotExist:
            return None

    async def list_projects(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        projects = Project.objects(**query)
        return [project.to_dict() for project in projects]

    async def update_project_status(self, project_id: str, audit_state: int) -> bool:
        try:
            project = Project.objects.get(id=project_id)
            project.audit_state = audit_state
            project.save()
            return True
        except Project.DoesNotExist:
            return False

    async def complete_project(self, project_id: str) -> bool:
        try:
            project = Project.objects.get(id=project_id)
            project.project_state = 0
            project.save()
            return True
        except Project.DoesNotExist:
            return False

    async def delete_project(self, project_id: str) -> bool:
        try:
            project = Project.objects.get(id=project_id)
            project.delete()
            return True
        except Project.DoesNotExist:
            return False