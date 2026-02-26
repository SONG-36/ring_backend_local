from abc import ABC, abstractmethod
from app.domain.models import HealthSummary

class HealthRepository(ABC):

    @abstractmethod
    def save(self, summary: HealthSummary):
        pass

    @abstractmethod
    def get_all(self):
        pass