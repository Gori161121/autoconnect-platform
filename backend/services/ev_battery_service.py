"""
EV Battery Service

Responsible for:
- Battery health scoring
- Charging efficiency analysis
- Range estimation analysis
- Battery risk assessment
"""


def calculate_battery_health_score(
    battery_health: int,
    charging_cycles: int,
    battery_temperature: int
) -> int:

    score = battery_health

    if charging_cycles > 1500:
        score -= 15
    elif charging_cycles > 1000:
        score -= 10
    elif charging_cycles > 700:
        score -= 5

    if battery_temperature > 45:
        score -= 15
    elif battery_temperature > 38:
        score -= 8

    return max(score, 0)


def determine_battery_risk_level(
    health_score: int
) -> str:

    if health_score >= 85:
        return "LOW"

    if health_score >= 60:
        return "MEDIUM"

    return "HIGH"


def estimate_battery_degradation(
    charging_cycles: int
) -> float:

    return round(
        charging_cycles * 0.02,
        2
    )


def build_ev_battery_summary(
    battery_health: int,
    charging_cycles: int,
    battery_temperature: int,
    estimated_range_km: int
):

    score = calculate_battery_health_score(
        battery_health,
        charging_cycles,
        battery_temperature
    )

    return {
        "battery_health_score": score,
        "risk_level": determine_battery_risk_level(score),
        "estimated_degradation_percent":
            estimate_battery_degradation(
                charging_cycles
            ),
        "estimated_range_km":
            estimated_range_km
    }
