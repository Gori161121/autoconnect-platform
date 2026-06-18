package mobile.android;

public class VehicleDashboardModel {

    private int vehicleHealthScore;
    private String riskLevel;

    private int driverScore;

    private int batteryHealth;

    private String insuranceRisk;

    public VehicleDashboardModel(
            int vehicleHealthScore,
            String riskLevel,
            int driverScore,
            int batteryHealth,
            String insuranceRisk
    ) {
        this.vehicleHealthScore = vehicleHealthScore;
        this.riskLevel = riskLevel;
        this.driverScore = driverScore;
        this.batteryHealth = batteryHealth;
        this.insuranceRisk = insuranceRisk;
    }

    public int getVehicleHealthScore() {
        return vehicleHealthScore;
    }

    public String getRiskLevel() {
        return riskLevel;
    }

    public int getDriverScore() {
        return driverScore;
    }

    public int getBatteryHealth() {
        return batteryHealth;
    }

    public String getInsuranceRisk() {
        return insuranceRisk;
    }
}
