package mobile.android;

public class AutoConnectApiClient {

    private final String baseUrl;

    public AutoConnectApiClient(String baseUrl) {
        this.baseUrl = baseUrl;
    }

    public String getVehicleHealthEndpoint(int vehicleId) {
        return baseUrl + "/vehicles/" + vehicleId + "/health";
    }

    public String getDiagnosticsEndpoint(int vehicleId) {
        return baseUrl + "/vehicles/" + vehicleId + "/diagnostics";
    }

    public String getIntelligenceReportEndpoint(int vehicleId) {
        return baseUrl + "/vehicles/" + vehicleId + "/intelligence-report";
    }
}
