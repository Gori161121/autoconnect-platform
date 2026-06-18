#include <iostream>
#include <string>
#include <vector>

struct TelemetryPayload {
    std::string vin;
    int mileage;
    int rpm;
    int engineTemperature;
    float batteryVoltage;
    bool checkEngine;
};

bool isEngineTemperatureCritical(int temperature) {
    return temperature >= 105;
}

bool isBatteryVoltageLow(float voltage) {
    return voltage < 12.0;
}

std::vector<std::string> analyzeTelemetry(const TelemetryPayload& payload) {
    std::vector<std::string> alerts;

    if (isEngineTemperatureCritical(payload.engineTemperature)) {
        alerts.push_back("ENGINE_TEMPERATURE_CRITICAL");
    }

    if (isBatteryVoltageLow(payload.batteryVoltage)) {
        alerts.push_back("BATTERY_VOLTAGE_LOW");
    }

    if (payload.checkEngine) {
        alerts.push_back("CHECK_ENGINE_ACTIVE");
    }

    return alerts;
}

int main() {
    TelemetryPayload payload = {
        "WAUZZZ8V5KA123456",
        128450,
        1850,
        108,
        11.7,
        true
    };

    std::vector<std::string> alerts = analyzeTelemetry(payload);

    std::cout << "Telemetry alerts:" << std::endl;

    for (const auto& alert : alerts) {
        std::cout << "- " << alert << std::endl;
    }

    return 0;
}
