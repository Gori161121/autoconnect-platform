from backend.services.vehicle_health_service import (
    calculate_vehicle_health_score,
    determine_vehicle_risk_level
)


def test_vehicle_health_score():

    score = calculate_vehicle_health_score(
        mileage=120000,
        active_fault_codes=1,
        overdue_services=1
    )

    assert score > 0


def test_vehicle_risk_level():

    result = determine_vehicle_risk_level(
        90
    )

    assert result == "LOW"
