from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class MongoManager:
    client: AsyncIOMotorClient = None
    db = None

    async def connect_to_database(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]
        
    async def close_database_connection(self):
        if self.client:
            self.client.close()
    
    def get_collection(self, collection_name: str):
        return self.db[collection_name]
    
    async def create_indexes(self):
        # 创建索引的示例
        await self.db.users.create_index("email", unique=True)
        await self.db.users.create_index("username", unique=True)

mongo = MongoManager()