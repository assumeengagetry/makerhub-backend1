from fastapi import APIRouter, HTTPException, Depends
from app.models.t5ask_model import Task
from app.services.t5ask_service import TaskService
from app.core.auth import require_super  # 引入超级管理员权限检查
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()
task_service = TaskService()

class TaskCreate(BaseModel):
    task_id: str
    department: str
    task_name: str
    name: str
    content: str
    deadline: datetime

@router.post("/tasks", summary="创建任务")
async def create_task(
    task: TaskCreate,
    current_user = Depends(require_super)  # 只允许最高权限用户
):
    result = await task_service.create_task(Task(**task.dict()))
    return {"code": 200, "data": {"id": result["id"]}}

@router.put("/tasks/{task_id}", summary="更新任务状态")
async def update_task_status(
    task_id: str,
    state: int,
    current_user = Depends(require_super)  # 只允许最高权限用户
):
    success = await task_service.update_task_status(task_id, state)
    if not success:
        raise HTTPException(status_code=404, detail="任务不存在")
    return {
        "code": 200,
        "data": {
            "task_id": task_id,
            "state": state
        }
    }

@router.get("/tasks", summary="获取任务列表")
async def get_tasks(
    current_user = Depends(require_super)  # 只允许最高权限用户
):
    tasks = await task_service.get_tasks()
    return {"code": 200, "data": tasks}