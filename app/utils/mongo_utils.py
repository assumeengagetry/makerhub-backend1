from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from loguru import logger

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    async def connect_to_database(self):
        logger.info("正在连接到MongoDB...")
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client[settings.MONGO_DB]
        logger.info("MongoDB连接成功")

    async def close_database_connection(self):
        logger.info("正在关闭MongoDB连接...")
        if self.client:
            self.client.close()
            logger.info("MongoDB连接已关闭")

    async def create_indexes(self):
        """创建必要的索引"""
        logger.info("正在创建MongoDB索引...")
        # 用户集合索引
        await self.db.users.create_index("userid", unique=True)
        # 值班记录索引
        await self.db.duty_records.create_index("userid")
        # 借用记录索引
        await self.db.borrow_records.create_index("apply_id", unique=True)
        logger.info("MongoDB索引创建完成")

mongo = MongoDB()