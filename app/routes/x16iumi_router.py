from fastapi import APIRouter, HTTPException, Depends
from app.models.x16iumi_model import XiumiLink
from app.services.x16iumi_service import XiumiService
from app.core.auth import AuthMiddleware, require_admin
from pydantic import BaseModel

router = APIRouter()
xiumi_service = XiumiService()

class XiumiLinkCreate(BaseModel):
    name: str
    userid: str
    link: str

@router.post("/xiumi-link", summary="创建宣传链接")
async def create_xiumi_link(
    link: XiumiLinkCreate,
    current_user = Depends(require_admin)  # 不允许最低等级用户创建
):
    result = await xiumi_service.create_link(XiumiLink(**link.dict()))
    return {"message": "宣传链接创建成功", "id": result["id"]}

@router.get("/xiumi-links", summary="获取所有宣传链接")
async def get_xiumi_links(
    current_user = Depends(require_admin)  # 只允许管理员获取
):
    links = await xiumi_service.get_links()
    return {"code": 200, "data": links}

@router.get("/xiumi-links/user/{userid}", summary="获取用户的宣传链接")
async def get_user_xiumi_links(
    userid: str,
    current_user = Depends(require_admin)  # 只允许管理员获取
):
    links = await xiumi_service.get_user_links(userid)
    return {"code": 200, "data": links}
