"""
Diagnostics Service

Responsible for:
- OBD fault code interpretation
- Diagnostic severity classification
- Vehicle issue prioritization
"""

FAULT_CODE_DATABASE = {
    "P0420": {
        "system": "Emissions",
        "severity": "MEDIUM",
        "description": "Catalyst system efficiency below threshold",
        "recommended_action": "Inspect catalytic converter and oxygen sensors"
    },
    "P0300": {
        "system": "Engine",
        "severity": "HIGH",
        "description": "Random or multiple cylinder misfire detected",
        "recommended_action": "Check ignition coils, spark plugs and fuel system"
    },
    "P0171": {
        "system": "Fuel System",
        "severity": "MEDIUM",
        "description": "System too lean",
        "recommended_action": "Inspect intake leaks, fuel pressure and oxygen sensors"
    },
    "P0562": {
        "system": "Electrical",
        "severity": "HIGH",
        "description": "System voltage low",
        "recommended_action": "Check battery, alternator and charging system"
    }
}


def interpret_fault_code(code: str) -> dict:
    return FAULT_CODE_DATABASE.get(
        code,
        {
            "system": "Unknown",
            "severity": "UNKNOWN",
            "description": "Fault code is not available in local database",
            "recommended_action": "Run full vehicle diagnostic scan"
        }
    )


def classify_vehicle_diagnostic_status(fault_codes: list) -> str:
    if not fault_codes:
        return "HEALTHY"

    severities = [
        interpret_fault_code(code)["severity"]
        for code in fault_codes
    ]

    if "HIGH" in severities:
        return "CRITICAL_ATTENTION_REQUIRED"

    if "MEDIUM" in severities:
        return "SERVICE_RECOMMENDED"

    return "MONITOR"
