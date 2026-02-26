from app.domain.models import UserHealthData

def calculate_base_score(user_data: UserHealthData) -> int:
    """
    只负责计算基础分数
    """

    sleep_score = user_data.sleep_hours * 10
    step_score = (user_data.steps_walked // 1000) * 5

    total = sleep_score + step_score

    if total > 100:
        total = 100

    return total