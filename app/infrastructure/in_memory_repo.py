from app.infrastructure.repository import HealthRepository
from app.domain.models import HealthSummary

class InMemoryHealthRepository(HealthRepository):

    def __init__(self):
        self._storage = []

    def save(self, summary: HealthSummary):
        self._storage.append(summary)

    def get_all(self):
        return self._storage