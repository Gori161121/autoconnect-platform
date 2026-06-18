"""
Maintenance Prediction Service

Responsible for:
- Maintenance urgency scoring
- Service due prediction
- Preventive maintenance recommendations
"""


def calculate_maintenance_urgency(
    oil_change_due_km: int,
    inspection_due_days: int,
    tire_rotation_due_km: int
) -> str:

    if oil_change_due_km <= 500:
        return "HIGH"

    if inspection_due_days <= 14:
        return "HIGH"

    if tire_rotation_due_km <= 1000:
        return "MEDIUM"

    if oil_change_due_km <= 1500:
        return "MEDIUM"

    return "LOW"


def generate_maintenance_recommendations(
    oil_change_due_km: int,
    inspection_due_days: int,
    tire_rotation_due_km: int
) -> list:

    recommendations = []

    if oil_change_due_km <= 1500:
        recommendations.append(
            "Oil change should be scheduled soon."
        )

    if inspection_due_days <= 30:
        recommendations.append(
            "Vehicle inspection deadline is approaching."
        )

    if tire_rotation_due_km <= 3000:
        recommendations.append(
            "Tire rotation should be planned."
        )

    if not recommendations:
        recommendations.append(
            "No urgent maintenance action required."
        )

    return recommendations


def build_maintenance_prediction(
    oil_change_due_km: int,
    inspection_due_days: int,
    tire_rotation_due_km: int
) -> dict:

    return {
        "urgency": calculate_maintenance_urgency(
            oil_change_due_km,
            inspection_due_days,
            tire_rotation_due_km
        ),
        "recommendations": generate_maintenance_recommendations(
            oil_change_due_km,
            inspection_due_days,
            tire_rotation_due_km
        )
    }
