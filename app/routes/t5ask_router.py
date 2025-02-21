from fastapi import APIRouter, HTTPException
from app.models.t5ask_model import Task
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class TaskCreate(BaseModel):
    task_id: str
    department: str
    task_name: str
    name: str
    content: str
    deadline: datetime

@router.post("/task")
async def create_task(task: TaskCreate):
    new_task =  Task(**task.dict(), state=0).save()
    return {"message": "任务创建成功", "id": str(new_task.id)}

@router.put("/task/{task_id}")
async def update_task_status(task_id: str, state: int):
    task =  Task.objects(task_id=task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="任务不存在")
    task.state = state
    task.save()
    return {"message": "任务状态更新成功"}