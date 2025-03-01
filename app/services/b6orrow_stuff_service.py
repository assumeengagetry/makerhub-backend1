from typing import List, Optional
from datetime import datetime
from loguru import logger
from app.models.b6orrow_stuff_model import BorrowRecord

class BorrowService:
    """借用服务类"""
    
    async def create_borrow(self, borrow_data: dict) -> dict:
        """创建借用记录"""
        try:
            borrow = BorrowRecord(**borrow_data)
            borrow.state = 0  # 未审核状态
            borrow.save()
            return {"id": str(borrow.id)}
        except Exception as e:
            logger.error(f"创建借用记录失败: {e}")
            raise

    async def update_borrow_status(self, borrow_id: str, state: int) -> bool:
        """更新借用状态"""
        try:
            borrow = BorrowRecord.objects(id=borrow_id).first()
            if not borrow:
                return False
            borrow.state = state
            borrow.save()
            return True
        except Exception as e:
            logger.error(f"更新借用状态失败: {e}")
            raise

    async def get_borrows(self, filters: dict = None) -> List[dict]:
        """获取借用记录列表"""
        try:
            query = filters or {}
            borrows = BorrowRecord.objects(**query).order_by('-created_at')
            return [borrow.to_dict() for borrow in borrows]
        except Exception as e:
            logger.error(f"获取借用记录失败: {e}")
            raise