from app.domain.models import UserHealthData
from app.domain.health_decision import calculate_health_score
from app.infrastructure.repository import HealthRepository


class SummaryService:

    def __init__(self, repository: HealthRepository):
        self.repository = repository

    def generate_summary(self, user_data_input):

        domain_data = UserHealthData(
            sleep_hours=user_data_input.sleep_hours,
            steps_walked=user_data_input.steps_walked
        )

        result = calculate_health_score(domain_data)

        self.repository.save(result)

        return {
            "health_score": result.score,
            "message": result.message
        }

    def get_history(self):
        history = self.repository.get_all()

        return [
            {
                "health_score": item.score,
                "message": item.message
            }
            for item in history
        ]