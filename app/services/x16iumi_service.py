from typing import List
from app.models.x16iumi_model import XiumiLink

class XiumiService:
    async def create_link(self, link_data: dict) -> dict:
        try:
            link = XiumiLink(**link_data)
            link.save()
            return {"id": str(link.id)}
        except Exception as e:
            logger.error(f"创建宣传链接失败: {e}")
            raise

    async def get_links(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        links = XiumiLink.objects(**query).order_by("-created_at")
        return [link.to_dict() for link in links]

    async def delete_link(self, link_id: str) -> bool:
        try:
            link = XiumiLink.objects.get(id=link_id)
            link.delete()
            return True
        except XiumiLink.DoesNotExist:
            return False

    async def get_user_links(self, userid: str) -> List[dict]:
        return await self.get_links({"userid": userid})