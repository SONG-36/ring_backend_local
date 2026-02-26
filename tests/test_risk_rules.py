from app.domain.risk_rules import evaluate_risk


def test_excellent():
    assert evaluate_risk(85) == "健康状态优秀"


def test_good():
    assert evaluate_risk(65) == "健康评分良好"


def test_bad():
    assert evaluate_risk(40) == "健康评分较差"