from fastapi import APIRouter, HTTPException, Depends
from app.models.p9roject_model import Project
from app.services.p9roject_service import ProjectService
from app.core.auth import AuthMiddleware, require_admin
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()
project_service = ProjectService()

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

@router.post("/project", status_code=201, summary="创建项目")
async def create_project(
    project: ProjectCreate,
    current_user = Depends(AuthMiddleware.get_current_user)
):
    result = await project_service.create_project(Project(**project.dict()))
    return {"message": "项目创建成功", "id": result["id"]}

@router.get("/project/{apply_id}", summary="获取单个项目")
async def get_project(
    apply_id: str,
    current_user = Depends(AuthMiddleware.get_current_user)
):
    project = await project_service.get_project(apply_id)
    if not project:
        raise HTTPException(status_code=404, detail="项目不存在")
    return project

@router.get("/projects/{state}", summary="按状态获取项目")
async def get_projects_by_state(
    state: str,
    current_user = Depends(AuthMiddleware.get_current_user)
):
    return await project_service.list_projects({"project_state": state})

@router.get("/projects", summary="获取所有项目")
async def get_projects(
    current_user = Depends(require_admin)
):
    return await project_service.list_projects()

@router.put("/project/{apply_id}", summary="更新项目状态")
async def update_project(
    apply_id: str,
    audit_state: Optional[int] = None,
    project_state: Optional[int] = None,
    current_user = Depends(require_admin)
):
    if audit_state is not None:
        await project_service.update_project_status(apply_id, audit_state)
    if project_state is not None:
        await project_service.complete_project(apply_id)
    return {"message": "项目更新成功"}

@router.delete("/project/{apply_id}", summary="删除项目")
async def delete_project(
    apply_id: str,
    current_user = Depends(require_admin)
):
    success = await project_service.delete_project(apply_id)
    if not success:
        raise HTTPException(status_code=404, detail="项目不存在")
    return {"message": "项目删除成功"}