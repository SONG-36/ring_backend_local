from app.domain.models import UserHealthData, HealthSummary
from app.domain.scoring_engine import calculate_base_score
from app.domain.risk_rules import evaluate_risk

def calculate_health_score(user_data: UserHealthData) -> HealthSummary:
    """
    现在只做整合调度
    """

    score = calculate_base_score(user_data)

    message = evaluate_risk(score)

    return HealthSummary(
        score=score,
        message=message
    )