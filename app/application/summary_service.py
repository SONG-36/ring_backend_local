from app.domain.models import UserHealthData
from app.domain.health_decision import calculate_health_score
from app.infrastructure.repository import HealthRepository
from app.external.llm_service import LLMService
from app.utils.response import AppError

class SummaryService:

    def __init__(self, repository: HealthRepository, llm_service: LLMService):
        self.repository = repository
        self.llm_service = llm_service

    def generate_summary(self, user_data_input):

        if user_data_input.sleep_hours < 0:
            raise AppError(code=4001, message="睡眠时间不能为负数", http_status=400)

        domain_data = UserHealthData(
            sleep_hours=user_data_input.sleep_hours,
            steps_walked=user_data_input.steps_walked
        )

        result = calculate_health_score(domain_data)

        # 调用 LLM 生成报告
        report = self.llm_service.generate_report(
            result.score,
            result.message
        )

        self.repository.save(result)

        return {
            "health_score": result.score,
            "message": result.message,
            "report": report
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