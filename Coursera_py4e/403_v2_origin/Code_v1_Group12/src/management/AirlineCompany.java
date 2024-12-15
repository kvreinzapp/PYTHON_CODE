
package management;

import reservation.Flight;
import java.time.Duration;
import java.util.*;

/**
 * 航空公司类
 * 修改说明：
 * 1. 删除了继承关系，改用接口实现
 * 2. 删除了重复的companyName字段
 * 3. 所有方法改为使用Flight对象而不是flightNumber
 * 4. 添加了异常处理
 */
public class AirlineCompany implements AdminCenter {
    private final String id;
    private final String name;
    private final List<Flight> flights;

    public AirlineCompany(String id, String name) {
        if (id == null || id.trim().isEmpty()) {
            throw new IllegalArgumentException("Company ID cannot be null or empty");
        }
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Company name cannot be null or empty");
        }

        this.id = id;
        this.name = name;
        this.flights = new ArrayList<>();
    }

    @Override
    public void performManagement() {
        try {
            generateFlightReport();
        } catch (Exception e) {
            throw new RuntimeException("Failed to perform management tasks", e);
        }
    }

    public void addFlight(Flight flight) {
        if (flight == null) {
            throw new IllegalArgumentException("Flight cannot be null");
        }
        if (flights.stream().anyMatch(f -> f.getFlightNumber().equals(flight.getFlightNumber()))) {
            throw new IllegalArgumentException("Flight number already exists");
        }

        try {
            flights.add(flight);
        } catch (Exception e) {
            throw new RuntimeException("Failed to add flight", e);
        }
    }

    public void cancelFlight(Flight flight) {
        if (flight == null) {
            throw new IllegalArgumentException("Flight cannot be null");
        }

        try {
            if (flights.remove(flight)) {
                flight.cancel();
            } else {
                throw new IllegalArgumentException("Flight not found");
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to cancel flight", e);
        }
    }

    public void delayFlight(Flight flight, Duration delay) {
        if (flight == null) {
            throw new IllegalArgumentException("Flight cannot be null");
        }
        if (delay == null) {
            throw new IllegalArgumentException("Delay duration cannot be null");
        }

        try {
            if (flights.contains(flight)) {
                flight.delay(delay);
            } else {
                throw new IllegalArgumentException("Flight not found");
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to delay flight", e);
        }
    }

    private void generateFlightReport() {
        System.out.println("Flight Report for " + name);
        flights.forEach(flight -> System.out.println(flight.getFlightDetails()));
    }

    // Getters
    public String getId() { return id; }
    public String getName() { return name; }
    public List<Flight> getFlights() { return Collections.unmodifiableList(flights); }
}