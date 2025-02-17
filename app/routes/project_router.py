from fastapi import APIRouter, HTTPException
from app.models.project_model import Project
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()

class ProjectCreate(BaseModel):
    apply_id: str
    project_name: str
    director: str
    college: str
    major_grade: str
    phone_num: str
    email: str
    mentor: str
    description: Optional[str] = ""
    application_file: Optional[str] = ""
    prove_file: Optional[str] = ""
    member: Optional[List[str]] = []
    start_time: datetime
    end_time: datetime

@router.post("/project", status_code=201)
async def create_project(project: ProjectCreate):
    try:
        new_project = Project(**project.dict()).save()
        return {"message": "项目创建成功", "id": str(new_project.id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/project/{apply_id}")
async def get_project(apply_id: str):
    project = Project.objects(apply_id=apply_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="项目不存在")
    return project.to_dict()

@router.put("/project/{apply_id}")
async def update_project(apply_id: str, audit_state: Optional[str] = None, project_state: Optional[str] = None):
    project = Project.objects(apply_id=apply_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="项目不存在")
    
    if audit_state:
        project.audit_state = audit_state
    if project_state:
        project.project_state = project_state
    
    project.save()
    return {"message": "项目更新成功"}

@router.get("/projects")
async def get_projects():
    projects = Project.objects()
    return [project.to_dict() for project in projects]