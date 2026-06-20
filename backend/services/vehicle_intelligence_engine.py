import json
from pathlib import Path

from backend.services.vehicle_health_service import generate_health_summary
from backend.services.diagnostics_service import classify_vehicle_diagnostic_status
from backend.services.driver_behavior_service import build_driver_behavior_summary
from backend.services.insurance_risk_service import build_insurance_risk_summary
from backend.services.maintenance_prediction_service import build_maintenance_prediction


SCENARIOS_DIR = Path(__file__).resolve().parents[2] / "data" / "scenarios"


def load_vehicle_scenario(filename: str) -> dict:
    scenario_path = SCENARIOS_DIR / filename

    with open(scenario_path, "r", encoding="utf-8") as file:
        return json.load(file)


def build_vehicle_intelligence_report(
    scenario_filename: str = "critical_engine_issue.json"
) -> dict:
    scenario = load_vehicle_scenario(scenario_filename)

    vehicle = scenario.get("vehicle", {})
    signals = scenario.get("signals", {})

    fault_codes = signals.get("fault_codes", [])

    health = generate_health_summary(
        mileage=vehicle.get("mileage", 0),
        active_fault_codes=len(fault_codes),
        overdue_services=1
    )

    diagnostics_status = classify_vehicle_diagnostic_status(
        fault_codes
    )

    driver = build_driver_behavior_summary(
        hard_brakes=signals.get("hard_brakes", 2),
        rapid_accelerations=signals.get("rapid_accelerations", 3),
        overspeed_events=signals.get("overspeed_events", 1)
    )

    insurance = build_insurance_risk_summary(
        driver_score=driver["driver_score"],
        active_fault_codes=len(fault_codes),
        accident_count=0
    )

    maintenance = build_maintenance_prediction(
        oil_change_due_km=signals.get("oil_change_due_km", 1500),
        inspection_due_days=signals.get("inspection_due_days", 30),
        tire_rotation_due_km=signals.get("tire_rotation_due_km", 2500),
        diagnostics_status=diagnostics_status
    )

    return {
        "scenario": scenario.get("title"),
        "vehicle": vehicle,
        "vehicle_health": health,
        "diagnostics_status": diagnostics_status,
        "driver_behavior": driver,
        "insurance_risk": insurance,
        "maintenance": maintenance
    }
