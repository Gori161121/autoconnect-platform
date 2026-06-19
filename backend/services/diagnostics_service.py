"""
Diagnostics Service

Uses an external DTC knowledge base instead of hardcoded fault codes.
"""

import json
from pathlib import Path


DTC_DATABASE_PATH = Path("data/dtc_codes.json")


def load_dtc_database() -> list:
    with open(DTC_DATABASE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def interpret_fault_code(code: str) -> dict:
    dtc_codes = load_dtc_database()

    for item in dtc_codes:
        if item["code"] == code:
            return item

    return {
        "code": code,
        "description": "Fault code is not available in local database",
        "system": "Unknown",
        "severity": "UNKNOWN",
        "recommended_action": "Run full diagnostic scan"
    }


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
