from app.domain.models import UserHealthData, HealthSummary

def calculate_health_score(user_data: UserHealthData) -> HealthSummary:
    """
    Domain 层核心业务逻辑
    """

    score = (user_data.sleep_hours * 10) + (user_data.steps_walked // 1000) * 5

    if score > 100:
        score = 100

    message = "健康评分良好" if score > 70 else "健康评分较差"

    return HealthSummary(
        score=score,
        message=message
    )