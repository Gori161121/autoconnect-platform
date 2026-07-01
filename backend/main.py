from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from backend.services.vehicle_health_service import generate_health_summary
from backend.services.diagnostics_service import (
    interpret_fault_code,
    classify_vehicle_diagnostic_status,
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
from backend.services.ai_insight_service import generate_vehicle_insight

app = FastAPI(
    title="AutoConnect Vehicle Intelligence API",
    description=(
        "Connected vehicle intelligence prototype: diagnostics, vehicle health, "
        "maintenance prediction, driver analytics, ownership intelligence, "
        "AI-explained fault codes and service recommendations."
    ),
    version="0.3.0",
)


class Vehicle(BaseModel):
    id: int
    vin: str
    make: str
    model: str
    year: int
    mileage: int
    vehicle_type: str  # ICE | EV | HYBRID


# --- In-memory fleet + per-vehicle telemetry -------------------------------

VEHICLES = [
    Vehicle(id=1, vin="WAUZZZ8V5KA123456", make="Audi", model="A3",
            year=2019, mileage=128450, vehicle_type="ICE"),
    Vehicle(id=2, vin="5YJ3E1EA7KF317000", make="Tesla", model="Model 3",
            year=2021, mileage=84500, vehicle_type="EV"),
    Vehicle(id=3, vin="JTDKN3DU5F0123456", make="Toyota", model="Prius",
            year=2018, mileage=142000, vehicle_type="HYBRID"),
]

TELEMETRY = {
    1: {
        "fault_codes": ["P0420"],
        "overdue_services": 1,
        "oil_change_due_km": 1500,
        "inspection_due_days": 32,
        "tire_rotation_due_km": 3000,
        "driver": {"hard_brakes": 2, "rapid_accelerations": 3, "overspeed_events": 1},
        "accident_count": 1,
    },
    2: {
        "fault_codes": [],
        "overdue_services": 0,
        "oil_change_due_km": 9999,
        "inspection_due_days": 120,
        "tire_rotation_due_km": 8000,
        "driver": {"hard_brakes": 1, "rapid_accelerations": 2, "overspeed_events": 0},
        "accident_count": 0,
        "ev": {"battery_health": 88, "charging_cycles": 740,
               "battery_temperature": 34, "estimated_range_km": 310},
    },
    3: {
        "fault_codes": ["P0171"],
        "overdue_services": 1,
        "oil_change_due_km": 800,
        "inspection_due_days": 20,
        "tire_rotation_due_km": 1500,
        "driver": {"hard_brakes": 3, "rapid_accelerations": 2, "overspeed_events": 2},
        "accident_count": 0,
        "hybrid": {"fuel_consumption_l_100km": 5.6, "electric_range_km": 42,
                   "battery_usage_percent": 68},
    },
}


def get_vehicle(vehicle_id: int) -> Vehicle:
    for vehicle in VEHICLES:
        if vehicle.id == vehicle_id:
            return vehicle
    raise HTTPException(status_code=404, detail="Vehicle not found")


def get_telemetry(vehicle_id: int) -> dict:
    get_vehicle(vehicle_id)  # 404 if missing
    return TELEMETRY.get(vehicle_id, {})


# --- Meta ------------------------------------------------------------------

@app.get("/")
def root():
    return {
        "project": "AutoConnect",
        "positioning": "Connected Vehicle Intelligence Platform",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


# --- Fleet -----------------------------------------------------------------

@app.get("/vehicles", response_model=List[Vehicle])
def list_vehicles():
    return VEHICLES


@app.get("/vehicles/{vehicle_id}", response_model=Vehicle)
def get_vehicle_detail(vehicle_id: int):
    return get_vehicle(vehicle_id)


# --- Vehicle intelligence --------------------------------------------------

@app.get("/vehicles/{vehicle_id}/health")
def vehicle_health(vehicle_id: int):
    vehicle = get_vehicle(vehicle_id)
    telemetry = get_telemetry(vehicle_id)
    return generate_health_summary(
        mileage=vehicle.mileage,
        active_fault_codes=len(telemetry.get("fault_codes", [])),
        overdue_services=telemetry.get("overdue_services", 0),
    )


@app.get("/vehicles/{vehicle_id}/diagnostics")
def vehicle_diagnostics(vehicle_id: int):
    telemetry = get_telemetry(vehicle_id)
    fault_codes = telemetry.get("fault_codes", [])
    return {
        "vehicle_id": vehicle_id,
        "status": classify_vehicle_diagnostic_status(fault_codes),
        "faults": [interpret_fault_code(code) for code in fault_codes],
    }


@app.get("/vehicles/{vehicle_id}/maintenance-prediction")
def maintenance_prediction(vehicle_id: int):
    telemetry = get_telemetry(vehicle_id)
    return build_maintenance_prediction(
        oil_change_due_km=telemetry.get("oil_change_due_km", 1500),
        inspection_due_days=telemetry.get("inspection_due_days", 30),
        tire_rotation_due_km=telemetry.get("tire_rotation_due_km", 3000),
    )


@app.get("/vehicles/{vehicle_id}/ev-battery")
def ev_battery_summary(vehicle_id: int):
    telemetry = get_telemetry(vehicle_id)
    ev = telemetry.get("ev")
    if not ev:
        raise HTTPException(status_code=400, detail="Vehicle is not an EV")
    return build_ev_battery_summary(**ev)


@app.get("/vehicles/{vehicle_id}/driver-behavior")
def driver_behavior(vehicle_id: int):
    telemetry = get_telemetry(vehicle_id)
    driver = telemetry.get("driver", {})
    return build_driver_behavior_summary(
        hard_brakes=driver.get("hard_brakes", 0),
        rapid_accelerations=driver.get("rapid_accelerations", 0),
        overspeed_events=driver.get("overspeed_events", 0),
    )


@app.get("/vehicles/{vehicle_id}/hybrid-efficiency")
def hybrid_efficiency(vehicle_id: int):
    telemetry = get_telemetry(vehicle_id)
    hybrid = telemetry.get("hybrid")
    if not hybrid:
        raise HTTPException(status_code=400, detail="Vehicle is not a hybrid")
    return build_hybrid_efficiency_summary(**hybrid)


@app.get("/vehicles/{vehicle_id}/valuation")
def vehicle_valuation(vehicle_id: int):
    vehicle = get_vehicle(vehicle_id)
    health = vehicle_health(vehicle_id)
    return build_vehicle_valuation_summary(
        original_price=30000,
        age_years=max(0, 2026 - vehicle.year),
        mileage=vehicle.mileage,
        health_score=health.get("health_score", 80),
    )


@app.get("/vehicles/{vehicle_id}/insurance-risk")
def insurance_risk(vehicle_id: int):
    telemetry = get_telemetry(vehicle_id)
    driver = build_driver_behavior_summary(
        hard_brakes=telemetry.get("driver", {}).get("hard_brakes", 0),
        rapid_accelerations=telemetry.get("driver", {}).get("rapid_accelerations", 0),
        overspeed_events=telemetry.get("driver", {}).get("overspeed_events", 0),
    )
    return build_insurance_risk_summary(
        driver_score=driver["driver_score"],
        active_fault_codes=len(telemetry.get("fault_codes", [])),
        accident_count=telemetry.get("accident_count", 0),
    )


@app.get("/vehicles/{vehicle_id}/intelligence-report")
def vehicle_intelligence_report(vehicle_id: int):
    get_vehicle(vehicle_id)
    return build_vehicle_intelligence_report()


@app.get("/vehicles/{vehicle_id}/ai-insight")
def vehicle_ai_insight(vehicle_id: int):
    vehicle = get_vehicle(vehicle_id)
    telemetry = get_telemetry(vehicle_id)
    fault_codes = telemetry.get("fault_codes", [])
    payload = {
        "vehicle": vehicle.model_dump(),
        "diagnostics": {
            "status": classify_vehicle_diagnostic_status(fault_codes),
            "faults": [interpret_fault_code(code) for code in fault_codes],
        },
        "health": generate_health_summary(
            mileage=vehicle.mileage,
            active_fault_codes=len(fault_codes),
            overdue_services=telemetry.get("overdue_services", 0),
        ),
    }
    return generate_vehicle_insight(payload)


# --- Services & ownership --------------------------------------------------

@app.get("/services/recommendations")
def service_recommendations():
    providers = [
        {"name": "AutoFix Service", "rating": 4.8, "distance_km": 4.5,
         "specialization_match": True, "estimated_price": 180},
        {"name": "Quick Garage", "rating": 4.4, "distance_km": 12,
         "specialization_match": False, "estimated_price": 120},
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
        months=12,
    )


# --- Legacy marketplace layer (isolated; kept for reference) ----------------

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


LEGACY_CUSTOMERS = [
    LegacyCustomer(id=1, full_name="John Smith", status="active"),
    LegacyCustomer(id=2, full_name="Emma Brown", status="active"),
]
LEGACY_PROVIDERS = [
    LegacyProvider(id=1, business_name="AutoFix Service",
                   category="Automotive Service", rating=4.8),
    LegacyProvider(id=2, business_name="Quick Garage",
                   category="Vehicle Maintenance", rating=4.6),
]
LEGACY_BOOKINGS = [
    LegacyBooking(id=1, customer_id=1, provider_id=1,
                  service_name="Engine Diagnostic Service", status="completed"),
]


@app.get("/legacy/customers", response_model=List[LegacyCustomer])
def legacy_customers():
    return LEGACY_CUSTOMERS


@app.get("/legacy/providers", response_model=List[LegacyProvider])
def legacy_providers():
    return LEGACY_PROVIDERS


@app.get("/legacy/bookings", response_model=List[LegacyBooking])
def legacy_bookings():
    return LEGACY_BOOKINGS


@app.get("/legacy/marketplace/summary")
def legacy_marketplace_summary():
    return {
        "customers": len(LEGACY_CUSTOMERS),
        "providers": len(LEGACY_PROVIDERS),
        "bookings": len(LEGACY_BOOKINGS),
        "status": "legacy_service_fulfillment_layer",
    }
