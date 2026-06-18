package mobile.android;

public class VehicleDiagnosticModel {

    private String faultCode;
    private String system;
    private String severity;
    private String description;
    private String recommendedAction;

    public VehicleDiagnosticModel(
            String faultCode,
            String system,
            String severity,
            String description,
            String recommendedAction
    ) {
        this.faultCode = faultCode;
        this.system = system;
        this.severity = severity;
        this.description = description;
        this.recommendedAction = recommendedAction;
    }

    public String getFaultCode() {
        return faultCode;
    }

    public String getSystem() {
        return system;
    }

    public String getSeverity() {
        return severity;
    }

    public String getDescription() {
        return description;
    }

    public String getRecommendedAction() {
        return recommendedAction;
    }
}
