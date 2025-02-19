from fastapi import APIRouter, HTTPException
from app.models.c10ompetition_model import Competition
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

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

@router.post("/competition")
async def create_competition(competition: CompetitionCreate):
    new_competition = await Competition(**competition.dict()).save()
    return {"message": "比赛创建成功", "id": str(new_competition.id)}

@router.get("/competitions")
async def get_competitions():
    competitions = await Competition.objects().all()
    return [comp.dict() for comp in competitions]