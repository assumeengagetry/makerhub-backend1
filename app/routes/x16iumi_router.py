from fastapi import APIRouter, HTTPException
from app.models.x16iumi_model import XiumiLink
from pydantic import BaseModel

router = APIRouter()

class XiumiLinkCreate(BaseModel):
    name: str
    userid: str
    link: str

@router.post("/xiumi-link")
async def create_xiumi_link(link: XiumiLinkCreate):
    new_link = await XiumiLink(**link.dict()).save()
    return {"message": "宣传链接创建成功", "id": str(new_link.id)}

@router.get("/xiumi-links")
async def get_xiumi_links():
    links = await XiumiLink.objects().all()
    return [link.dict() for link in links]

@router.delete("/xiumi-link/{link_id}")
async def delete_xiumi_link(link_id: str):
    link = await XiumiLink.objects(id=link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="宣传链接不存在")
    await link.delete()
    return {"message": "宣传链接删除成功"}