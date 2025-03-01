from typing import Optional
from app.models.r2egulation_model import Regulation
from mongoengine.errors import DoesNotExist, ValidationError

class RegulationService:
    async def get_regulation(self, regulation_id: str) -> Optional[dict]:
        try:
            regulation = Regulation.objects.get(id=regulation_id)
            return regulation.to_dict()
        except (DoesNotExist, ValidationError):
            return None