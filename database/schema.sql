-- AutoConnect Platform
-- Marketplace Database Schema v1

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(30),
    email VARCHAR(100),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE providers (
    id SERIAL PRIMARY KEY,
    business_name VARCHAR(120) NOT NULL,
    category VARCHAR(80) NOT NULL,
    rating DECIMAL(3,2) DEFAULT 0,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    provider_id INTEGER REFERENCES providers(id),
    service_name VARCHAR(120) NOT NULL,
    category VARCHAR(80),
    base_price DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    provider_id INTEGER REFERENCES providers(id),
    service_id INTEGER REFERENCES services(id),
    booking_date DATE NOT NULL,
    status VARCHAR(30) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    booking_id INTEGER REFERENCES bookings(id),
    rating INTEGER,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE matching_recommendations (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    provider_id INTEGER REFERENCES providers(id),
    score DECIMAL(5,2),
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_provider ON bookings(provider_id);
CREATE INDEX idx_services_provider ON services(provider_id);
CREATE INDEX idx_recommendations_customer ON matching_recommendations(customer_id);
-- ==========================================
-- Connected Vehicle Intelligence Tables
-- ==========================================

CREATE TABLE vehicles (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES customers(id),
    vin VARCHAR(50) UNIQUE NOT NULL,
    make VARCHAR(80),
    model VARCHAR(80),
    year INTEGER,
    mileage INTEGER,
    status VARCHAR(30) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE obd_devices (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES vehicles(id),
    device_serial VARCHAR(100) UNIQUE NOT NULL,
    firmware_version VARCHAR(50),
    connection_status VARCHAR(30) DEFAULT 'inactive',
    last_sync_at TIMESTAMP
);

CREATE TABLE diagnostic_events (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES vehicles(id),
    fault_code VARCHAR(20),
    severity VARCHAR(30),
    description TEXT,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) DEFAULT 'open'
);

CREATE TABLE maintenance_records (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES vehicles(id),
    service_type VARCHAR(100),
    service_date DATE,
    mileage_at_service INTEGER,
    cost DECIMAL(10,2),
    notes TEXT
);

CREATE TABLE ownership_costs (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES vehicles(id),
    cost_type VARCHAR(80),
    amount DECIMAL(10,2),
    cost_date DATE,
    notes TEXT
);

CREATE TABLE vehicle_health_snapshots (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES vehicles(id),
    health_score INTEGER,
    risk_level VARCHAR(30),
    active_fault_codes INTEGER,
    overdue_services INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_vehicles_owner ON vehicles(owner_id);
CREATE INDEX idx_diagnostics_vehicle ON diagnostic_events(vehicle_id);
CREATE INDEX idx_maintenance_vehicle ON maintenance_records(vehicle_id);
CREATE INDEX idx_ownership_vehicle ON ownership_costs(vehicle_id);
