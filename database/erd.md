# Entity Relationship Diagram

```mermaid
erDiagram

    customers {
        int id PK
        string full_name
        string phone
        string email
        string status
        timestamp created_at
    }

    providers {
        int id PK
        string business_name
        string category
        decimal rating
        string status
        timestamp created_at
    }

    services {
        int id PK
        int provider_id FK
        string service_name
        string category
        decimal base_price
        boolean is_active
    }

    bookings {
        int id PK
        int customer_id FK
        int provider_id FK
        int service_id FK
        date booking_date
        string status
        timestamp created_at
    }

    reviews {
        int id PK
        int booking_id FK
        int rating
        string feedback
        timestamp created_at
    }

    matching_recommendations {
        int id PK
        int customer_id FK
        int provider_id FK
        decimal score
        string reason
        timestamp created_at
    }

    vehicles {
        int id PK
        int owner_id FK
        string vin
        string make
        string model
        int year
        int mileage
        string status
        timestamp created_at
    }

    obd_devices {
        int id PK
        int vehicle_id FK
        string device_serial
        string firmware_version
        string connection_status
        timestamp last_sync_at
    }

    diagnostic_events {
        int id PK
        int vehicle_id FK
        string fault_code
        string severity
        string description
        timestamp detected_at
        string status
    }

    maintenance_records {
        int id PK
        int vehicle_id FK
        string service_type
        date service_date
        int mileage_at_service
        decimal cost
        string notes
    }

    ownership_costs {
        int id PK
        int vehicle_id FK
        string cost_type
        decimal amount
        date cost_date
        string notes
    }

    vehicle_health_snapshots {
        int id PK
        int vehicle_id FK
        int health_score
        string risk_level
        int active_fault_codes
        int overdue_services
        timestamp created_at
    }

    ev_battery_snapshots {
        int id PK
        int vehicle_id FK
        int battery_health
        int charging_cycles
        int battery_temperature
        int estimated_range_km
        string risk_level
        timestamp created_at
    }

    driver_behavior_events {
        int id PK
        int vehicle_id FK
        int hard_brakes
        int rapid_accelerations
        int overspeed_events
        int driver_score
        string behavior_classification
        timestamp created_at
    }

    hybrid_efficiency_snapshots {
        int id PK
        int vehicle_id FK
        decimal fuel_consumption_l_100km
        int electric_range_km
        int battery_usage_percent
        int efficiency_score
        string classification
        timestamp created_at
    }

    vehicle_valuations {
        int id PK
        int vehicle_id FK
        decimal original_price
        decimal estimated_value
        string classification
        timestamp created_at
    }

    insurance_risk_profiles {
        int id PK
        int vehicle_id FK
        int driver_score
        int active_fault_codes
        int accident_count
        int insurance_risk_score
        string classification
        decimal premium_multiplier
        timestamp created_at
    }

    providers ||--o{ services : offers
    customers ||--o{ bookings : creates
    providers ||--o{ bookings : receives
    services ||--o{ bookings : booked_for
    bookings ||--o{ reviews : generates
    customers ||--o{ matching_recommendations : receives
    providers ||--o{ matching_recommendations : recommended

    customers ||--o{ vehicles : owns
    vehicles ||--o{ obd_devices : connects
    vehicles ||--o{ diagnostic_events : generates
    vehicles ||--o{ maintenance_records : has
    vehicles ||--o{ ownership_costs : creates
    vehicles ||--o{ vehicle_health_snapshots : generates
    vehicles ||--o{ ev_battery_snapshots : generates
    vehicles ||--o{ driver_behavior_events : generates
    vehicles ||--o{ hybrid_efficiency_snapshots : generates
    vehicles ||--o{ vehicle_valuations : generates
    vehicles ||--o{ insurance_risk_profiles : generates
```    driver_behavior_events {
        int id PK
        int vehicle_id FK
        int hard_brakes
        int rapid_accelerations
        int overspeed_events
        int driver_score
        string behavior_classification
    }

    hybrid_efficiency_snapshots {
        int id PK
        int vehicle_id FK
        decimal fuel_consumption_l_100km
        int electric_range_km
        int battery_usage_percent
        int efficiency_score
        string classification
    }

    vehicle_valuations {
        int id PK
        int vehicle_id FK
        decimal original_price
        decimal estimated_value
        string classification
    }

    insurance_risk_profiles {
        int id PK
        int vehicle_id FK
        int driver_score
        int active_fault_codes
        int accident_count
        int insurance_risk_score
        decimal premium_multiplier
    }

    vehicles ||--o{ ev_battery_snapshots : generates
    vehicles ||--o{ driver_behavior_events : generates
    vehicles ||--o{ hybrid_efficiency_snapshots : generates
    vehicles ||--o{ vehicle_valuations : generates
    vehicles ||--o{ insurance_risk_profiles : generates
