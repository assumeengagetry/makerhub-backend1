from typing import List, Optional
from app.models.p3rinter_model import PrinterApplication

class PrinterService:
    async def create_print_request(self, request_data: dict) -> dict:
        request = PrinterApplication(**request_data)
        request.state = 0  # 未审核状态
        request.save()
        return {"id": str(request.id)}

    async def update_print_status(self, request_id: str, state: int, reason: str = None) -> bool:
        try:
            request = PrinterApplication.objects.get(id=request_id)
            request.state = state
            if reason:
                request.reason = reason
            request.save()
            return True
        except PrinterApplication.DoesNotExist:
            return False

    async def get_print_request(self, request_id: str) -> Optional[dict]:
        try:
            request = PrinterApplication.objects.get(id=request_id)
            return request.to_dict()
        except PrinterApplication.DoesNotExist:
            return None

    async def list_print_requests(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        requests = PrinterApplication.objects(**query)
        return [request.to_dict() for request in requests]