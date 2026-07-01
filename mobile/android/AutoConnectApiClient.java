package com.autoconnect.android;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;

/**
 * Minimal HTTP client for the AutoConnect Vehicle Intelligence API.
 * Uses the JDK HttpClient (no third-party dependencies).
 */
public class AutoConnectApiClient {
    private final String baseUrl;
    private final HttpClient httpClient;

    public AutoConnectApiClient(String baseUrl) {
        this.baseUrl = baseUrl.endsWith("/")
            ? baseUrl.substring(0, baseUrl.length() - 1)
            : baseUrl;
        this.httpClient = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(10))
            .build();
    }

    /** Perform a GET request and return the raw JSON body. */
    public String get(String path) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + path))
            .timeout(Duration.ofSeconds(15))
            .header("Accept", "application/json")
            .GET()
            .build();

        HttpResponse<String> response =
            httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() >= 400) {
            throw new IOException("Request failed: HTTP " + response.statusCode());
        }
        return response.body();
    }

    public String getVehicles() throws IOException, InterruptedException {
        return get("/vehicles");
    }

    public String getDiagnostics(int vehicleId) throws IOException, InterruptedException {
        return get("/vehicles/" + vehicleId + "/diagnostics");
    }

    public String getHealth(int vehicleId) throws IOException, InterruptedException {
        return get("/vehicles/" + vehicleId + "/health");
    }

    public String getAiInsight(int vehicleId) throws IOException, InterruptedException {
        return get("/vehicles/" + vehicleId + "/ai-insight");
    }
}
