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
from backend.services.vehicle_valuation_service import build_vehicle_valuation_summary
from backend.services.insurance_risk_service import build_insurance_risk_summary
from backend.services.vehicle_intelligence_engine import build_vehicle_intelligence_report


app = FastAPI(
    title="AutoConnect Vehicle Intelligence API",
    description="Connected vehicle intelligence prototype for diagnostics, vehicle health, maintenance prediction, driver analytics, ownership intelligence and service recommendations.",
    version="0.2.0"
)


class Vehicle(BaseModel):
    id: int
    vin: str
    make: str
    model: str
    year: int
    mileage: int
    vehicle_type: str


class LegacyCustomer(BaseModel):
    id: int
    full_name: str
    status: str


class LegacyProvider(BaseModel):
    id: int
    business_name: str
    category: str
    rating: float


class LegacyBooking(BaseModel):
    id: int
    customer_id: int
    provider_id: int
    service_name: str
    status: str


vehicles = [
    Vehicle(
        id=1,
        vin="WAUZZZ8V5KA123456",
        make="Audi",
        model="A3",
        year=2019,
        mileage=128450,
        vehicle_type="ICE"
    ),
    Vehicle(
        id=2,
        vin="5YJ3E1EA7KF317000",
        make="Tesla",
        model="Model 3",
        year=2021,
        mileage=84500,
        vehicle_type="EV"
    ),
    Vehicle(
        id=3,
        vin="JTDKN3DU5F0123456",
        make="Toyota",
        model="Prius",
        year=2018,
        mileage=142000,
        vehicle_type="HYBRID"
    )
]


legacy_customers = [
    LegacyCustomer(id=1, full_name="John Smith", status="active"),
    LegacyCustomer(id=2, full_name="Emma Brown", status="active")
]


legacy_providers = [
    LegacyProvider(
        id=1,
        business_name="AutoFix Service",
        category="Automotive Service",
        rating=4.8
    ),
    LegacyProvider(
        id=2,
        business_name="Quick Garage",
        category="Vehicle Maintenance",
        rating=4.6
    )
]


legacy_bookings = [
    LegacyBooking(
        id=1,
        customer_id=1,
        provider_id=1,
        service_name="Engine Diagnostic Service",
        status="completed"
    )
]


@app.get("/")
def root():
    return {
        "project": "AutoConnect",
        "positioning": "Connected Vehicle Intelligence Platform",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/vehicles", response_model=List[Vehicle])
def get_vehicles():
    return vehicles


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


# Legacy marketplace layer
# Kept temporarily as a service fulfillment layer for future automotive service booking.


@app.get("/legacy/customers", response_model=List[LegacyCustomer])
def get_legacy_customers():
    return legacy_customers


@app.get("/legacy/providers", response_model=List[LegacyProvider])
def get_legacy_providers():
    return legacy_providers


@app.get("/legacy/bookings", response_model=List[LegacyBooking])
def get_legacy_bookings():
    return legacy_bookings


@app.get("/legacy/marketplace/summary")
def legacy_marketplace_summary():
    return {
        "customers": len(legacy_customers),
        "providers": len(legacy_providers),
        "bookings": len(legacy_bookings),
        "status": "legacy_service_fulfillment_layer"
    }class Provider(BaseModel):
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
