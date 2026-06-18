from backend.services.diagnostics_service import (
    interpret_fault_code,
    classify_vehicle_diagnostic_status
)


def test_interpret_known_fault_code():
    result = interpret_fault_code("P0420")

    assert result["system"] == "Emissions"
    assert result["severity"] == "MEDIUM"


def test_interpret_unknown_fault_code():
    result = interpret_fault_code("X9999")

    assert result["system"] == "Unknown"


def test_diagnostic_status_high():
    result = classify_vehicle_diagnostic_status(["P0300"])

    assert result == "CRITICAL_ATTENTION_REQUIRED"


def test_diagnostic_status_healthy():
    result = classify_vehicle_diagnostic_status([])

    assert result == "HEALTHY"
