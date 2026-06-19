from backend.services.diagnostics_service import (
    interpret_fault_code,
    classify_vehicle_diagnostic_status
)


def test_known_fault_code():

    result = interpret_fault_code(
        "P0300"
    )

    assert result["system"] == "Engine"
    assert result["severity"] == "HIGH"


def test_unknown_fault_code():

    result = interpret_fault_code(
        "P9999"
    )

    assert result["severity"] == "UNKNOWN"


def test_healthy_vehicle():

    result = classify_vehicle_diagnostic_status(
        []
    )

    assert result == "HEALTHY"


def test_critical_vehicle():

    result = classify_vehicle_diagnostic_status(
        ["P0300"]
    )

    assert result == "CRITICAL_ATTENTION_REQUIRED"


def test_service_recommended():

    result = classify_vehicle_diagnostic_status(
        ["P0420"]
    )

    assert result == "SERVICE_RECOMMENDED"
