package com.autoconnect.android;

/** Driver behaviour metrics and derived score. */
public class DriverBehaviorModel {
    public int hardBrakes;
    public int rapidAccelerations;
    public int overspeedEvents;
    public int driverScore;      // 0-100
    public String classification; // SAFE | MODERATE | RISKY

    public DriverBehaviorModel(int hardBrakes, int rapidAccelerations,
                               int overspeedEvents, int driverScore,
                               String classification) {
        this.hardBrakes = hardBrakes;
        this.rapidAccelerations = rapidAccelerations;
        this.overspeedEvents = overspeedEvents;
        this.driverScore = driverScore;
        this.classification = classification;
    }
}
