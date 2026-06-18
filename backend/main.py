from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from backend.services.vehicle_health_service import generate_health_summary
from backend.services.diagnostics_service import (
    interpret_fault_code,
    classify_vehicle_diagnostic_status
)
from backend.services.maintenance_prediction_service import build_maintenance_prediction
from backend.services.service_recommendation_engine import recommend_service_provider
from backend.services.ownership_cost_analytics import build_cost_summary
from backend.services.ev_battery_service import build_ev_battery_summary
from backend.services.driver_behavior_service import build_driver_behavior_summary
from backend.services.hybrid_efficiency_service import build_hybrid_efficiency_summary
from backend.services.vehicle_valuation_service import (
    build_vehicle_valuation_summary
)
from backend.services.insurance_risk_service import (
    build_insurance_risk_summary
)
from backend.services.vehicle_intelligence_engine import (
    build_vehicle_intelligence_report
)


app = FastAPI(
    title="AutoConnect Platform API",
    description="Marketplace platform connecting customers and service providers.",
    version="0.1.0"
)

class Customer(BaseModel):
    id: int
    full_name: str
    status: str

class Provider(BaseModel):
    id: int
    business_name: str
    category: str
    rating: float

class Booking(BaseModel):
    id: int
    customer_id: int
    provider_id: int
    service_name: str
    status: str

customers = [
    Customer(id=1, full_name="John Smith", status="active"),
    Customer(id=2, full_name="Emma Brown", status="active")
]

providers = [
    Provider(
        id=1,
        business_name="Elite Cleaning",
        category="Home Services",
        rating=4.8
    ),
    Provider(
        id=2,
        business_name="Quick Repairs",
        category="Maintenance",
        rating=4.6
    )
]

bookings = [
    Booking(
        id=1,
        customer_id=1,
        provider_id=1,
        service_name="Apartment Cleaning",
        status="completed"
    )
]

@app.get("/")
def root():
    return {
        "project": "AutoConnect Platform",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/customers", response_model=List[Customer])
def get_customers():
    return customers

@app.get("/providers", response_model=List[Provider])
def get_providers():
    return providers

@app.get("/bookings", response_model=List[Booking])
def get_bookings():
    return bookings

@app.get("/marketplace/summary")
def marketplace_summary():
    return {
        "customers": len(customers),
        "providers": len(providers),
        "bookings": len(bookings),
        "platform_status": "active"
    }
@app.get("/vehicles")
def get_vehicles():
    return [
        {
            "id": 1,
            "vin": "WAUZZZ8V5KA123456",
            "make": "Audi",
            "model": "A3",
            "year": 2019,
            "mileage": 128450
        }
    ]


@app.get("/vehicles/{vehicle_id}/health")
def vehicle_health(vehicle_id: int):
    return generate_health_summary(
        mileage=128450,
        active_fault_codes=1,
        overdue_services=1
    )


@app.get("/vehicles/{vehicle_id}/diagnostics")
def vehicle_diagnostics(vehicle_id: int):
    fault_codes = ["P0420"]

    return {
        "vehicle_id": vehicle_id,
        "status": classify_vehicle_diagnostic_status(fault_codes),
        "faults": [
            interpret_fault_code(code)
            for code in fault_codes
        ]
    }


@app.get("/vehicles/{vehicle_id}/maintenance-prediction")
def maintenance_prediction(vehicle_id: int):
    return build_maintenance_prediction(
        oil_change_due_km=1500,
        inspection_due_days=32,
        tire_rotation_due_km=3000
    )


@app.get("/services/recommendations")
def service_recommendations():
    providers = [
        {
            "name": "AutoFix Service",
            "rating": 4.8,
            "distance_km": 4.5,
            "specialization_match": True,
            "estimated_price": 180
        },
        {
            "name": "Quick Garage",
            "rating": 4.4,
            "distance_km": 12,
            "specialization_match": False,
            "estimated_price": 120
        }
    ]

    return recommend_service_provider(providers)


@app.get("/ownership/cost-summary")
def ownership_cost_summary():
    return build_cost_summary(
        fuel_cost=1200,
        maintenance_cost=650,
        insurance_cost=900,
        inspection_cost=120,
        parking_cost=300,
        fines_cost=80,
        months=12
    )
@app.get("/vehicles/{vehicle_id}/ev-battery")
def ev_battery_summary(vehicle_id: int):
    return build_ev_battery_summary(
        battery_health=88,
        charging_cycles=740,
        battery_temperature=34,
        estimated_range_km=310
    )
@app.get("/vehicles/{vehicle_id}/driver-behavior")
def driver_behavior(vehicle_id: int):
    return build_driver_behavior_summary(
        hard_brakes=2,
        rapid_accelerations=3,
        overspeed_events=1
    )
@app.get("/vehicles/{vehicle_id}/hybrid-efficiency")
def hybrid_efficiency(vehicle_id: int):
    return build_hybrid_efficiency_summary(
        fuel_consumption_l_100km=5.6,
        electric_range_km=42,
        battery_usage_percent=68
    )
@app.get("/vehicles/{vehicle_id}/valuation")
def vehicle_valuation(vehicle_id: int):

    return build_vehicle_valuation_summary(
        original_price=30000,
        age_years=5,
        mileage=120000,
        health_score=85
    )
@app.get("/vehicles/{vehicle_id}/insurance-risk")
def insurance_risk(vehicle_id: int):

    return build_insurance_risk_summary(
        driver_score=85,
        active_fault_codes=1,
        accident_count=1
    )
@app.get("/vehicles/{vehicle_id}/intelligence-report")
def vehicle_intelligence_report(vehicle_id: int):
    return build_vehicle_intelligence_report()
