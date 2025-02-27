from fastapi import APIRouter, HTTPException
from loguru import logger
from app.services.u1ser_service import UserService
from app.core.config import settings
import aiohttp
from typing import Optional
from pydantic import BaseModel

router = APIRouter()
user_service = UserService()

class WxLoginRequest(BaseModel):
    code: str
    user_info: Optional[dict] = None

@router.post("/wx-login")
async def wx_login(request: WxLoginRequest):
    try:
        async with aiohttp.ClientSession() as session:
            # 请求微信接口获取openild
            async with session.get(
                settings.WECHAT_LOGIN_URL,
                
                params={
                    'appid': settings.WECHAT_APPID,
                    'secret': settings.WECHAT_SECRET,
                    'js_code': request.code,
                    'grant_type': 'authorization_code'
                }
            ) as response:
                wx_response = await response.json()
                
                if 'errcode' in wx_response:
                    raise HTTPException(
                        status_code=400,
                        detail=f"微信登录失败: {wx_response['errmsg']}"
                    )
                
                openid = wx_response['openid']
                
                # 处理用户信息
                result = await user_service.create_or_update_wx_user(
                    openid,
                    request.user_info or {}
                )
                return result
                
    except Exception as e:
        logger.error(f"微信登录处理失败: {str(e)}")
        raise HTTPException(status_code=500, detail="登录处理失败")