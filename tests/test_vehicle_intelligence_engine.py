from backend.services.vehicle_intelligence_engine import (
    build_vehicle_intelligence_report
)


def test_vehicle_intelligence_report():
    result = build_vehicle_intelligence_report()

    assert "vehicle_health" in result
    assert "diagnostics_status" in result
    assert "driver_behavior" in result
    assert "insurance_risk" in result
    assert "maintenance" in result
