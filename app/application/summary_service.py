from app.domain.models import UserHealthData
from app.domain.health_decision import calculate_health_score

def generate_summary(user_data_input):
    """
    Application 层：
    - 把 API DTO 转换成 Domain Model
    - 调用 Domain
    - 把 Domain 结果转成 JSON
    """

    # DTO → Domain Model
    domain_data = UserHealthData(
        sleep_hours=user_data_input.sleep_hours,
        steps_walked=user_data_input.steps_walked
    )

    # 调用 Domain
    result = calculate_health_score(domain_data)

    # Domain → JSON
    return {
        "health_score": result.score,
        "message": result.message
    }