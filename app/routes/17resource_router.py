from fastapi import APIRouter
from app.core.config import settings
from app.models.r17esource import Resource
from app.core.db import minio_client

router = APIRouter()

@router.get("/{resource_name}", response_model=Resource)
async def get_resource_url(resource_name: str):
    """
    获取资源的公共访问URL
    resource_name格式示例: 'logo.png', 'banner.jpg'
    """
    # 检查文件是否存在
    try:
        minio_client.client.stat_object(settings.MINIO_BUCKET, resource_name)
        return {
            "url": f"{settings.MINIO_PUBLIC_URL}/{settings.MINIO_BUCKET}/{resource_name}",
            "alt_text": resource_name
        }
    except:
        # 如果文件不存在，返回默认图片或占位符URL
        return {
            "url": f"{settings.MINIO_PUBLIC_URL}/{settings.MINIO_BUCKET}/placeholder.png",
            "alt_text": "Image not found"
        }
