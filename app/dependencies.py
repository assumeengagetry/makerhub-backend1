from typing import Generator
from fastapi import Depends, HTTPException, status
from app.utils.mongo_utils import mongo
from app.middleware.auth_middleware import get_current_user_id
from motor.motor_asyncio import AsyncIOMotorDatabase

async def get_db() -> Generator:
    try:
        yield mongo.db
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

async def get_current_user(
    db: AsyncIOMotorDatabase = Depends(get_db),
    user_id: str = Depends(get_current_user_id)
):
    user = await db.users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

def get_collection(collection_name: str):
    async def get_collection_dependency(db: AsyncIOMotorDatabase = Depends(get_db)):
        return db[collection_name]
    return get_collection_dependency