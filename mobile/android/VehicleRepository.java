package mobile.android;

public class VehicleRepository {

    private final AutoConnectApiClient apiClient;

    public VehicleRepository(AutoConnectApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public String fetchVehicleHealth(int vehicleId) {
        return apiClient.getVehicleHealthEndpoint(vehicleId);
    }

    public String fetchVehicleDiagnostics(int vehicleId) {
        return apiClient.getDiagnosticsEndpoint(vehicleId);
    }

    public String fetchVehicleIntelligenceReport(int vehicleId) {
        return apiClient.getIntelligenceReportEndpoint(vehicleId);
    }
}
