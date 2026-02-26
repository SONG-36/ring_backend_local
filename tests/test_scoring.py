from app.domain.models import UserHealthData
from app.domain.scoring_engine import calculate_base_score


def test_score_normal_case():
    user = UserHealthData(sleep_hours=7, steps_walked=5000)
    score = calculate_base_score(user)

    assert score == 7 * 10 + (5000 // 1000) * 5


def test_score_upper_bound():
    user = UserHealthData(sleep_hours=20, steps_walked=20000)
    score = calculate_base_score(user)

    assert score == 100