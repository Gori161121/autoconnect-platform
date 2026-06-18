from backend.services.vehicle_health_service import (
    generate_health_summary
)

from backend.services.diagnostics_service import (
    classify_vehicle_diagnostic_status
)

from backend.services.driver_behavior_service import (
    build_driver_behavior_summary
)

from backend.services.insurance_risk_service import (
    build_insurance_risk_summary
)

from backend.services.maintenance_prediction_service import (
    build_maintenance_prediction
)


def build_vehicle_intelligence_report():

    health = generate_health_summary(
        mileage=128450,
        active_fault_codes=1,
        overdue_services=1
    )

    diagnostics_status = classify_vehicle_diagnostic_status(
        ["P0420"]
    )

    driver = build_driver_behavior_summary(
        hard_brakes=2,
        rapid_accelerations=3,
        overspeed_events=1
    )

    insurance = build_insurance_risk_summary(
        driver_score=driver["driver_score"],
        active_fault_codes=1,
        accident_count=0
    )

    maintenance = build_maintenance_prediction(
        oil_change_due_km=1500,
        inspection_due_days=30,
        tire_rotation_due_km=2500
    )

    return {
        "vehicle_health": health,
        "diagnostics_status": diagnostics_status,
        "driver_behavior": driver,
        "insurance_risk": insurance,
        "maintenance": maintenance
    }
