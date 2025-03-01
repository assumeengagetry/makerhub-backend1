from typing import List, Optional
from loguru import logger
from app.models.c10ompetition_model import Competition

class CompetitionService:
    async def create_competition(self, competition_data: dict) -> dict:
        try:
            competition = Competition(**competition_data)
            competition.save()
            logger.info(f"比赛创建成功: {competition.id}")
            return {"id": str(competition.id)}
        except Exception as e:
            logger.error(f"创建比赛失败: {e}")
            raise

    async def get_competition(self, game_id: str) -> Optional[dict]:
        try:
            competition = Competition.objects.get(id=game_id)
            return competition.to_dict()
        except Competition.DoesNotExist:
            return None

    async def list_competitions(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        competitions = Competition.objects(**query).order_by("+registration_start")
        return [competition.to_dict() for competition in competitions]

    async def update_competition(self, game_id: str, game_data: dict) -> bool:
        try:
            competition = Competition.objects.get(id=game_id)
            for key, value in game_data.items():
                setattr(competition, key, value)
            competition.save()
            return True
        except Competition.DoesNotExist:
            return False

    async def delete_competition(self, game_id: str) -> bool:
        try:
            competition = Competition.objects.get(id=game_id)
            competition.delete()
            return True
        except Competition.DoesNotExist:
            return False