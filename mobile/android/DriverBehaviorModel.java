package mobile.android;

public class DriverBehaviorModel {

    private int driverScore;
    private String behavior;
    private int hardBrakes;
    private int rapidAccelerations;
    private int overspeedEvents;

    public DriverBehaviorModel(
            int driverScore,
            String behavior,
            int hardBrakes,
            int rapidAccelerations,
            int overspeedEvents
    ) {
        this.driverScore = driverScore;
        this.behavior = behavior;
        this.hardBrakes = hardBrakes;
        this.rapidAccelerations = rapidAccelerations;
        this.overspeedEvents = overspeedEvents;
    }

    public int getDriverScore() {
        return driverScore;
    }

    public String getBehavior() {
        return behavior;
    }

    public int getHardBrakes() {
        return hardBrakes;
    }

    public int getRapidAccelerations() {
        return rapidAccelerations;
    }

    public int getOverspeedEvents() {
        return overspeedEvents;
    }
}
