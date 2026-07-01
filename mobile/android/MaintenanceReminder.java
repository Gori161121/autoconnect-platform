package com.autoconnect.android;

/** A maintenance reminder item derived from the prediction service. */
public class MaintenanceReminder {
    public String title;
    public String urgency; // LOW | MEDIUM | HIGH
    public String detail;

    public MaintenanceReminder(String title, String urgency, String detail) {
        this.title = title;
        this.urgency = urgency;
        this.detail = detail;
    }

    public boolean isUrgent() {
        return "HIGH".equalsIgnoreCase(urgency);
    }
}
