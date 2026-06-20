# Mobile Layer

This directory contains prototype mobile application components for AutoConnect.

The goal is not to provide a complete Android or iOS application.

The purpose is to demonstrate how vehicle intelligence services can be consumed by mobile clients.

---

## Architecture

```text
Backend API
      ↓
API Client
      ↓
Repository Layer
      ↓
Mobile Models
      ↓
Dashboard / UI
```

---

## Android Components

### Models

- VehicleDashboardModel
- VehicleDiagnosticModel
- VehicleHealthModel
- VehicleIntelligenceReportModel
- InsuranceRiskModel

### Infrastructure

- AutoConnectApiClient
- VehicleRepository

---

## iOS Components

### Models

- VehicleDashboardModel
- VehicleDiagnosticModel
- VehicleHealthModel
- VehicleIntelligenceReportModel
- InsuranceRiskModel

### Infrastructure

- AutoConnectApiClient
- VehicleRepository

---

## Purpose

The mobile layer consumes information produced by:

- Diagnostics Service
- Vehicle Health Service
- Maintenance Prediction Service
- Driver Behavior Analytics
- Insurance Risk Service
- Vehicle Intelligence Engine

---

## Current Scope

The current implementation focuses on:

- domain models
- API access abstraction
- repository pattern

The following components are intentionally not implemented yet:

- UI screens
- authentication
- push notifications
- offline storage
- background synchronization

These are future product extensions.

---

## Position in AutoConnect

```text
Vehicle
   ↓
IoT / OBD Layer
   ↓
Backend Intelligence Layer
   ↓
Mobile Application
```
