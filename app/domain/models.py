from dataclasses import dataclass

@dataclass
class UserHealthData:
    sleep_hours: int
    steps_walked: int

@dataclass
class HealthSummary:
    score: int
    message: str