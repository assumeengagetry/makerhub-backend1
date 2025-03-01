from typing import List
from app.models.s7tuff_model import Stuff
from app.models.b6orrow_stuff_model import BorrowRecord

class StuffService:
    async def add_item(self, stuff_data: dict) -> dict:
        stuff = Stuff(**stuff_data)
        stuff.save()
        return {"id": str(stuff.id)}

    async def update_item_quantity(self, stuff_id: str, new_quantity: int) -> bool:
        try:
            stuff = Stuff.objects.get(id=stuff_id)
            stuff.number = new_quantity
            stuff.save()
            return True
        except Stuff.DoesNotExist:
            return False

    async def get_item_list(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        items = Stuff.objects(**query).order_by("-created_at")
        return [item.to_dict() for item in items]

    async def create_borrow_request(self, request_data: dict) -> dict:
        request = BorrowRecord(**request_data)
        request.state = 0  # 未审核状态
        request.save()
        return {"id": str(request.id)}

    async def get_borrow_records(self, user_id: str = None) -> List[dict]:
        query = {"userid": user_id} if user_id else {}
        records = BorrowRecord.objects(**query)
        return [record.to_dict() for record in records]