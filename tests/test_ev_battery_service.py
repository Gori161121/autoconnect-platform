from backend.services.ev_battery_service import (
    calculate_battery_health_score,
    determine_battery_risk_level,
    estimate_battery_degradation,
    build_ev_battery_summary
)


def test_battery_health_score():
    score = calculate_battery_health_score(
        battery_health=88,
        charging_cycles=740,
        battery_temperature=34
    )

    assert score == 83


def test_battery_risk_level():
    assert determine_battery_risk_level(90) == "LOW"


def test_battery_degradation():
    result = estimate_battery_degradation(500)

    assert result == 10.0


def test_ev_battery_summary():
    result = build_ev_battery_summary(
        battery_health=88,
        charging_cycles=740,
        battery_temperature=34,
        estimated_range_km=310
    )

    assert result["risk_level"] == "MEDIUM"
