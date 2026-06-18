package mobile.android;

public class MaintenanceReminder {

    private String serviceType;
    private int dueInKm;
    private int dueInDays;
    private String urgency;

    public MaintenanceReminder(
            String serviceType,
            int dueInKm,
            int dueInDays,
            String urgency
    ) {
        this.serviceType = serviceType;
        this.dueInKm = dueInKm;
        this.dueInDays = dueInDays;
        this.urgency = urgency;
    }

    public String getServiceType() {
        return serviceType;
    }

    public int getDueInKm() {
        return dueInKm;
    }

    public int getDueInDays() {
        return dueInDays;
    }

    public String getUrgency() {
        return urgency;
    }
}
