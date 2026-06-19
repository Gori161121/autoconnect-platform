import json
from pathlib import Path

from backend.services.vehicle_health_service import (
    generate_health_summary
)

from backend.services.diagnostics_service import (
    classify_vehicle_diagnostic_status
)


SCENARIOS_DIR = Path("data/scenarios")


def load_scenario(filename: str):
    path = SCENARIOS_DIR / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_critical_engine_issue():

    scenario = load_scenario(
        "critical_engine_issue.json"
    )

    signals = scenario["signals"]

    health = generate_health_summary(
        mileage=scenario["vehicle"]["mileage"],
        active_fault_codes=len(
            signals["fault_codes"]
        ),
        overdue_services=1
    )

    diagnostics = classify_vehicle_diagnostic_status(
        signals["fault_codes"]
    )

    return {
        "scenario": scenario["title"],
        "health": health,
        "diagnostics": diagnostics
    }


def main():

    report = run_critical_engine_issue()

    print("\n=== AUTOCONNECT DEMO ===\n")

    print(
        json.dumps(
            report,
            indent=4
        )
    )


if __name__ == "__main__":
    main()
