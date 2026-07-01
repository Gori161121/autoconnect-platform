package com.autoconnect.android;

import java.io.IOException;

/**
 * Repository layer: the app talks to this, and it talks to the API client.
 * Keeps networking out of the UI layer.
 */
public class VehicleRepository {
    private final AutoConnectApiClient apiClient;

    public VehicleRepository(AutoConnectApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /** Returns raw diagnostics JSON, or a safe empty result on failure. */
    public String loadDiagnostics(int vehicleId) {
        try {
            return apiClient.getDiagnostics(vehicleId);
        } catch (IOException | InterruptedException e) {
            return "{\"status\":\"UNAVAILABLE\",\"faults\":[]}";
        }
    }

    public String loadAiInsight(int vehicleId) {
        try {
            return apiClient.getAiInsight(vehicleId);
        } catch (IOException | InterruptedException e) {
            return "{\"summary\":\"Insight unavailable offline.\",\"recommendations\":[]}";
        }
    }
}
