package com.autoconnect.android;

/** Overall status of a vehicle shown on the dashboard. */
public class VehicleStatusModel {
    public int vehicleId;
    public String make;
    public String model;
    public int year;
    public int mileage;
    public String vehicleType; // ICE | EV | HYBRID

    public VehicleStatusModel(int vehicleId, String make, String model,
                              int year, int mileage, String vehicleType) {
        this.vehicleId = vehicleId;
        this.make = make;
        this.model = model;
        this.year = year;
        this.mileage = mileage;
        this.vehicleType = vehicleType;
    }

    public String displayName() {
        return year + " " + make + " " + model;
    }
}
