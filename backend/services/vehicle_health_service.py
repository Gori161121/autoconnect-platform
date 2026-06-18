"""
Vehicle Health Service

Responsible for:
- Vehicle health scoring
- Risk assessment
- Maintenance status evaluation
"""


def calculate_vehicle_health_score(
    mileage: int,
    active_fault_codes: int,
    overdue_services: int
) -> int:

    score = 100

    score -= min(active_fault_codes * 10, 40)

    score -= min(overdue_services * 15, 30)

    if mileage > 200000:
        score -= 15
    elif mileage > 120000:
        score -= 10
    elif mileage > 80000:
        score -= 5

    return max(score, 0)


def determine_vehicle_risk_level(
    health_score: int
) -> str:

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

    score = calculate_vehicle_health_score(
        mileage,
        active_fault_codes,
        overdue_services
    )

    return {
        "health_score": score,
        "risk_level": determine_vehicle_risk_level(score)
    }
