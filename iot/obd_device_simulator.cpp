// obd_device_simulator.cpp
// Simulates an OBD-II device streaming live telemetry (PIDs) as JSON lines.
// Represents the edge device that feeds the AutoConnect backend.
//
// Build: g++ -std=c++17 obd_device_simulator.cpp -o obd_sim
// Run:   ./obd_sim 5     (emit 5 telemetry samples)

#include <iostream>
#include <random>
#include <string>

struct Telemetry {
    int rpm;
    int speed_kmh;
    int coolant_temp_c;
    int throttle_pct;
    double fuel_level_pct;
};

Telemetry sample(std::mt19937& rng) {
    std::uniform_int_distribution<int> rpm(800, 4200);
    std::uniform_int_distribution<int> speed(0, 130);
    std::uniform_int_distribution<int> coolant(80, 105);
    std::uniform_int_distribution<int> throttle(0, 100);
    std::uniform_real_distribution<double> fuel(5.0, 100.0);
    return {rpm(rng), speed(rng), coolant(rng), throttle(rng), fuel(rng)};
}

std::string toJson(const Telemetry& t) {
    return "{\"rpm\":" + std::to_string(t.rpm) +
           ",\"speed_kmh\":" + std::to_string(t.speed_kmh) +
           ",\"coolant_temp_c\":" + std::to_string(t.coolant_temp_c) +
           ",\"throttle_pct\":" + std::to_string(t.throttle_pct) +
           ",\"fuel_level_pct\":" + std::to_string(t.fuel_level_pct) + "}";
}

int main(int argc, char* argv[]) {
    int samples = (argc > 1) ? std::stoi(argv[1]) : 3;
    std::mt19937 rng(42);  // fixed seed for reproducible output

    for (int i = 0; i < samples; ++i) {
        std::cout << toJson(sample(rng)) << "\n";
    }
    return 0;
}
