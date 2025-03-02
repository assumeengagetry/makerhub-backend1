from fastapi import APIRouter, HTTPException
from loguru import logger
from app.services.u1ser_service import UserService
from app.core.config import settings
import aiohttp
from typing import Optional, Dict, Any
from pydantic import BaseModel
import json
import requests

router = APIRouter()
user_service = UserService()

class WxLoginRequest(BaseModel):
    code: str


@router.post("/wx-login")
async def wx_login(request: WxLoginRequest):
    try:
        
            url = f"{settings.WECHAT_LOGIN_URL}?appid={settings.WECHAT_APPID}&secret={settings.WECHAT_SECRET}&js_code={request.code}&grant_type=authorization_code"
            
            
            logger.info({url})
            
            
            response = requests.get(url)
            wx_response = response.json()
            
            
            logger.info(wx_response)


            openid = wx_response.get("openid")
            
            
            logger.info(openid)
            
            
            return await user_service.create_or_update_wx_user(openid)
                                
                
    except Exception as e:
        logger.error(f"微信登录失败: {str(e)}")
        raise HTTPException(status_code=500, detail="登录失败",)
        



@router.get("/user")
async def get_user(openid: str):
    try:
        user = await user_service.get_user(openid)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "code": 200,
            "data": user
        }
    except Exception as e:
        logger.error(f"获取用户信息失败: {str(e)}")
        raise HTTPException(status_code=500, detail="获取用户信息失败")

@router.put("/real_name")
async def update_user_realname(openid: str, real_name: str):
    try:
        result = await user_service.update_user_realname(openid, real_name)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "code": 200,
            "message": "Real name updated successfully"
        }
    except Exception as e:
        logger.error(f"更新用户真实姓名失败: {str(e)}")
        raise HTTPException(status_code=500, detail="更新用户真实姓名失败")

