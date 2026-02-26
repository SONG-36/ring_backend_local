from abc import ABC, abstractmethod

class LLMService(ABC):

    @abstractmethod
    def generate_report(self, score: int, message: str) -> str:
        pass