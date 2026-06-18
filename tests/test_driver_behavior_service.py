from backend.services.driver_behavior_service import (
    calculate_driver_risk_score,
    classify_driver_behavior,
    build_driver_behavior_summary
)


def test_driver_risk_score():
    result = calculate_driver_risk_score(
        hard_brakes=2,
        rapid_accelerations=3,
        overspeed_events=1
    )

    assert result == 72


def test_driver_behavior_classification():
    assert classify_driver_behavior(90) == "SAFE"
    assert classify_driver_behavior(70) == "MODERATE"
    assert classify_driver_behavior(50) == "RISKY"


def test_driver_behavior_summary():
    result = build_driver_behavior_summary(
        hard_brakes=1,
        rapid_accelerations=1,
        overspeed_events=1
    )

    assert result["driver_score"] == 85
    assert result["behavior"] == "SAFE"
