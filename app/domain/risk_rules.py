def evaluate_risk(score: int) -> str:
    """
    只负责风险判断
    """

    if score >= 80:
        return "健康状态优秀"
    elif score >= 60:
        return "健康评分良好"
    else:
        return "健康评分较差"