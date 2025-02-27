from fastapi import APIRouter, HTTPException, Depends
from app.models.c10ompetition_model import Competition
from app.services.c10ompetition_service import CompetitionService
from app.core.auth import require_admin, AuthMiddleware
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()
competition_service = CompetitionService()

class CompetitionCreate(BaseModel):
    game_id: str
    name: str
    wx_num: str
    qq_num: str
    introduction: str
    registration_start: datetime
    registration_end: datetime
    contest_start: datetime
    contest_end: datetime
    link: str

@router.post("/competition", summary="创建比赛")
async def create_competition(
    competition: CompetitionCreate,
    _=Depends(require_admin)  # 需要管理员权限
):
    result = await competition_service.create_competition(Competition(**competition.dict()))
    return {"message": "比赛创建成功", "id": result["id"]}

@router.get("/competitions", summary="获取所有比赛")
async def get_competitions(
    current_user = Depends(AuthMiddleware.get_current_user)  # 允许所有登录用户访问
):
    return await competition_service.list_competitions()

@router.delete("/competition/{competition_id}", summary="删除比赛")
async def delete_competition(
    competition_id: str,
    _=Depends(require_admin)  # 需要管理员权限
):
    result = await competition_service.delete_competition(competition_id)
    if not result:
        raise HTTPException(status_code=404, detail="比赛不存在")
    return {"message": "比赛删除成功"}