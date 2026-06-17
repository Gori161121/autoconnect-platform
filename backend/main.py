from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

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
