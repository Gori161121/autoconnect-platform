"""
Vehicle Health Service

Responsible for:
- Vehicle health scoring
- Risk assessment
- Diagnostic score calculation
- Maintenance score calculation
- Mileage score calculation
"""


def calculate_diagnostic_score(active_fault_codes: int) -> int:
    score = 100 - min(active_fault_codes * 15, 60)
    return max(score, 0)


def calculate_maintenance_score(overdue_services: int) -> int:
    score = 100 - min(overdue_services * 20, 60)
    return max(score, 0)


def calculate_mileage_score(mileage: int) -> int:
    if mileage > 250000:
        return 50

    if mileage > 180000:
        return 65

    if mileage > 120000:
        return 75

    if mileage > 80000:
        return 85

    return 100


def calculate_vehicle_health_score(
    mileage: int,
    active_fault_codes: int,
    overdue_services: int
) -> int:
    diagnostic_score = calculate_diagnostic_score(active_fault_codes)
    maintenance_score = calculate_maintenance_score(overdue_services)
    mileage_score = calculate_mileage_score(mileage)

    final_score = (
        diagnostic_score * 0.4
        + maintenance_score * 0.35
        + mileage_score * 0.25
    )

    return round(final_score)


def determine_vehicle_risk_level(health_score: int) -> str:
    if health_score >= 85:
        return "LOW"

    if health_score >= 60:
        return "MEDIUM"

    return "HIGH"


def generate_health_summary(
    mileage: int,
    active_fault_codes: int,
    overdue_services: int
):
    diagnostic_score = calculate_diagnostic_score(active_fault_codes)
    maintenance_score = calculate_maintenance_score(overdue_services)
    mileage_score = calculate_mileage_score(mileage)

    health_score = calculate_vehicle_health_score(
        mileage,
        active_fault_codes,
        overdue_services
    )

    return {
        "health_score": health_score,
        "risk_level": determine_vehicle_risk_level(health_score),
        "score_breakdown": {
            "diagnostic_score": diagnostic_score,
            "maintenance_score": maintenance_score,
            "mileage_score": mileage_score
        }
    }
