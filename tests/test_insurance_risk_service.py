from backend.services.insurance_risk_service import (
    calculate_insurance_risk_score,
    classify_insurance_risk,
    build_insurance_risk_summary
)


def test_insurance_score():
    result = calculate_insurance_risk_score(
        driver_score=90,
        active_fault_codes=1,
        accident_count=0
    )

    assert result > 0


def test_insurance_classification():
    assert classify_insurance_risk(90) == "LOW_RISK"


def test_insurance_summary():
    result = build_insurance_risk_summary(
        driver_score=85,
        active_fault_codes=1,
        accident_count=1
    )

    assert "insurance_risk_score" in result
