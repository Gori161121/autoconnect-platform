#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

struct VehicleTelemetry {
    std::string vin;
    int mileage;
    int rpm;
    int engineTemperature;
    float batteryVoltage;
    bool checkEngine;
    std::string faultCode;
};

VehicleTelemetry generateTelemetry() {
    VehicleTelemetry data;

    data.vin = "WAUZZZ8V5KA123456";
    data.mileage = 128450;
    data.rpm = 850 + rand() % 2500;
    data.engineTemperature = 75 + rand() % 35;
    data.batteryVoltage = 11.8f + static_cast<float>(rand() % 20) / 10;
    data.checkEngine = rand() % 2 == 1;

    if (data.checkEngine) {
        data.faultCode = "P0420";
    } else {
        data.faultCode = "NONE";
    }

    return data;
}

void printTelemetryAsJson(const VehicleTelemetry& data) {
    std::cout << "{\n";
    std::cout << "  \"vin\": \"" << data.vin << "\",\n";
    std::cout << "  \"mileage\": " << data.mileage << ",\n";
    std::cout << "  \"rpm\": " << data.rpm << ",\n";
    std::cout << "  \"engine_temperature\": " << data.engineTemperature << ",\n";
    std::cout << "  \"battery_voltage\": " << data.batteryVoltage << ",\n";
    std::cout << "  \"check_engine\": " << (data.checkEngine ? "true" : "false") << ",\n";
    std::cout << "  \"fault_code\": \"" << data.faultCode << "\"\n";
    std::cout << "}\n";
}

int main() {
    srand(static_cast<unsigned int>(time(nullptr)));

    VehicleTelemetry telemetry = generateTelemetry();

    printTelemetryAsJson(telemetry);

    return 0;
}
