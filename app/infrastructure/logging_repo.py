from app.infrastructure.repository import HealthRepository
from app.domain.models import HealthSummary
import logging
logger = logging.getLogger(__name__)

class LoggingHealthRepository(HealthRepository):

    def save(self, summary: HealthSummary):
        logger.info(f"Saved: score={summary.score}, message={summary.message}")

    def get_all(self):
        logger.info("get_all called")
        return []