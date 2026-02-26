from app.infrastructure.repository import HealthRepository
from app.domain.models import HealthSummary

class LoggingHealthRepository(HealthRepository):

    def save(self, summary: HealthSummary):
        print(f"[LOGGING REPO] Saved: score={summary.score}, message={summary.message}")

    def get_all(self):
        print("[LOGGING REPO] get_all called")
        return []