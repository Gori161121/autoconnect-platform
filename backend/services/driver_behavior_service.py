"""
Driver Behavior Service

Responsible for:
- Driving behavior analysis
- Risk scoring
- Aggressive driving detection
"""


def calculate_driver_risk_score(
    hard_brakes: int,
    rapid_accelerations: int,
    overspeed_events: int
) -> int:

    score = 100

    score -= hard_brakes * 5
    score -= rapid_accelerations * 4
    score -= overspeed_events * 6

    return max(score, 0)


def classify_driver_behavior(
    risk_score: int
) -> str:

    if risk_score >= 85:
        return "SAFE"

    if risk_score >= 60:
        return "MODERATE"

    return "RISKY"


def build_driver_behavior_summary(
    hard_brakes: int,
    rapid_accelerations: int,
    overspeed_events: int
) -> dict:

    score = calculate_driver_risk_score(
        hard_brakes,
        rapid_accelerations,
        overspeed_events
    )

    return {
        "driver_score": score,
        "behavior": classify_driver_behavior(score),
        "hard_brakes": hard_brakes,
        "rapid_accelerations": rapid_accelerations,
        "overspeed_events": overspeed_events
    }
