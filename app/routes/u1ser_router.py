from fastapi import APIRouter, HTTPException
from loguru import logger
from app.services.u1ser_service import UserService
from app.core.config import settings
import aiohttp
from typing import Optional, Dict, Any
from pydantic import BaseModel
import json

router = APIRouter()
user_service = UserService()

class WxLoginRequest(BaseModel):
    code: str


@router.post("/wx-login")
async def wx_login(request: WxLoginRequest):
    try:
        async with aiohttp.ClientSession() as session:
            params = {
                'appid': settings.WECHAT_APPID,
                'secret': settings.WECHAT_SECRET,
                'js_code': request.code,
                'grant_type': 'authorization_code'
            }
            
            async with session.get(settings.WECHAT_LOGIN_URL, params=params) as response:
                wx_response = json.loads(await response.text())
                
                if wx_response.get('errcode', 0) != 0:
                    raise HTTPException(status_code=400, detail="微信登录失败")
                
                openid = wx_response.get('openid')
                if not openid:
                    raise HTTPException(status_code=400, detail="获取openid失败")

                return await user_service.create_or_update_wx_user(openid)
                                
                
    except Exception as e:
        logger.error(f"微信登录失败: {str(e)}")
        raise HTTPException(status_code=500, detail="登录失败")
    
@router.post("/forntend-login")
async def frontend_login(openid):
    try:
        return await user_service.create_or_update_wx_user(openid)
    except Exception :
        raise HTTPException(status_code=500, detail="登录失败")


