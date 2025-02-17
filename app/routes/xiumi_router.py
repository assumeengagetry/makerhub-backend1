from fastapi import APIRouter, HTTPException
from app.models.publicity_link_model import PublicityLink
from pydantic import BaseModel

router = APIRouter()

class XiumiLinkCreate(BaseModel):
    name: str
    userid: str
    link: str

@router.post("/xiumi-link")
async def create_xiumi_link(link: XiumiLinkCreate):
    new_link = await PublicityLink(**link.dict()).save()
    return {"message": "宣传链接创建成功", "id": str(new_link.id)}

@router.get("/xiumi-links")
async def get_xiumi_links():
    links = await PublicityLink.objects().all()
    return [link.dict() for link in links]

@router.delete("/xiumi-link/{link_id}")
async def delete_xiumi_link(link_id: str):
    link = await PublicityLink.objects(id=link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="宣传链接不存在")
    await link.delete()
    return {"message": "宣传链接删除成功"}