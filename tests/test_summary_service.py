from app.application.summary_service import SummaryService
from app.domain.models import HealthSummary


class FakeRepository:
    def __init__(self):
        self.saved = []

    def save(self, summary):
        self.saved.append(summary)

    def get_all(self):
        return self.saved


class FakeLLM:
    def generate_report(self, score, message):
        return "fake report"


class FakeUserData:
    def __init__(self, sleep_hours, steps_walked):
        self.sleep_hours = sleep_hours
        self.steps_walked = steps_walked


def test_generate_summary():

    repo = FakeRepository()
    llm = FakeLLM()

    service = SummaryService(repo, llm)

    user = FakeUserData(7, 5000)

    result = service.generate_summary(user)

    assert "health_score" in result
    assert "message" in result
    assert "report" in result

    assert len(repo.saved) == 1