package mobile.android;

public class VehicleStatusModel {

    private String vin;
    private int mileage;
    private int healthScore;
    private String riskLevel;
    private boolean checkEngine;

    public VehicleStatusModel(
            String vin,
            int mileage,
            int healthScore,
            String riskLevel,
            boolean checkEngine
    ) {
        this.vin = vin;
        this.mileage = mileage;
        this.healthScore = healthScore;
        this.riskLevel = riskLevel;
        this.checkEngine = checkEngine;
    }

    public String getVin() {
        return vin;
    }

    public int getMileage() {
        return mileage;
    }

    public int getHealthScore() {
        return healthScore;
    }

    public String getRiskLevel() {
        return riskLevel;
    }

    public boolean isCheckEngine() {
        return checkEngine;
    }
}
