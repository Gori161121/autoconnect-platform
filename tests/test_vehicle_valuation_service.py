from backend.services.vehicle_valuation_service import (
    estimate_vehicle_value,
    classify_vehicle_value,
    build_vehicle_valuation_summary
)


def test_estimate_vehicle_value():
    result = estimate_vehicle_value(
        original_price=30000,
        age_years=3,
        mileage=80000,
        health_score=90
    )

    assert result > 0


def test_classify_vehicle_value():
    assert classify_vehicle_value(
        25000,
        30000
    ) == "HIGH_RESALE_VALUE"


def test_vehicle_valuation_summary():
    result = build_vehicle_valuation_summary(
        original_price=30000,
        age_years=5,
        mileage=120000,
        health_score=85
    )

    assert "estimated_value" in result
