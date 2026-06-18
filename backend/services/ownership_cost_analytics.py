"""
Ownership Cost Analytics

Responsible for:
- Vehicle ownership cost tracking
- Annual ownership estimation
- Cost category breakdown
"""


def calculate_total_ownership_cost(
    fuel_cost: float,
    maintenance_cost: float,
    insurance_cost: float,
    inspection_cost: float,
    parking_cost: float,
    fines_cost: float
) -> float:

    return round(
        fuel_cost
        + maintenance_cost
        + insurance_cost
        + inspection_cost
        + parking_cost
        + fines_cost,
        2
    )


def calculate_monthly_average(
    total_cost: float,
    months: int
) -> float:

    if months <= 0:
        return 0

    return round(
        total_cost / months,
        2
    )


def build_cost_summary(
    fuel_cost: float,
    maintenance_cost: float,
    insurance_cost: float,
    inspection_cost: float,
    parking_cost: float,
    fines_cost: float,
    months: int
) -> dict:

    total = calculate_total_ownership_cost(
        fuel_cost,
        maintenance_cost,
        insurance_cost,
        inspection_cost,
        parking_cost,
        fines_cost
    )

    return {
        "total_cost": total,
        "monthly_average": calculate_monthly_average(
            total,
            months
        ),
        "fuel_cost": fuel_cost,
        "maintenance_cost": maintenance_cost,
        "insurance_cost": insurance_cost,
        "inspection_cost": inspection_cost,
        "parking_cost": parking_cost,
        "fines_cost": fines_cost
    }
