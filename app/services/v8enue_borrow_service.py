from typing import List, Optional
from app.models.v8enue_borrow_model import VenueBorrow

class VenueService:
    async def create_venue_request(self, request_data: dict) -> dict:
        request = VenueBorrow(**request_data)
        request.state = 0  # 待审核
        request.save()
        return {"id": str(request.id)}

    async def update_venue_status(self, request_id: str, state: int, reason: str = None) -> bool:
        try:
            request = VenueBorrow.objects.get(id=request_id)
            request.state = state
            if reason:
                request.reason = reason
            request.save()
            return True
        except VenueBorrow.DoesNotExist:
            return False

    async def get_venue_requests(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        requests = VenueBorrow.objects(**query).order_by("+start_time")
        return [request.to_dict() for request in requests]

    async def get_venue_request(self, apply_id: str) -> Optional[dict]:
        try:
            request = VenueBorrow.objects.get(id=apply_id)
            return request.to_dict()
        except VenueBorrow.DoesNotExist:
            return None