
package management;

import reservation.Flight;
import java.util.*;

/**
 * 航班时刻表类
 * 修改说明：
 * 1. 删除了继承关系，改用接口实现
 * 2. 简化了类的职责
 * 3. 添加了异常处理
 */
public class FlightSchedule implements AdminCenter {
    private final List<Flight> flights;

    public FlightSchedule() {
        this.flights = new ArrayList<>();
    }

    @Override
    public void performManagement() {
        try {
            displaySchedule();
        } catch (Exception e) {
            throw new RuntimeException("Failed to perform schedule management", e);
        }
    }

    public void addFlight(Flight flight) {
        if (flight == null) {
            throw new IllegalArgumentException("Flight cannot be null");
        }
        if (flights.stream().anyMatch(f -> f.getFlightNumber().equals(flight.getFlightNumber()))) {
            throw new IllegalArgumentException("Flight number already exists in schedule");
        }

        try {
            flights.add(flight);
        } catch (Exception e) {
            throw new RuntimeException("Failed to add flight to schedule", e);
        }
    }

    public void removeFlight(Flight flight) {
        if (flight == null) {
            throw new IllegalArgumentException("Flight cannot be null");
        }

        try {
            if (!flights.remove(flight)) {
                throw new IllegalArgumentException("Flight not found in schedule");
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to remove flight from schedule", e);
        }
    }

    private void displaySchedule() {
        System.out.println("\nCurrent Flight Schedule:");
        flights.forEach(flight -> System.out.println(flight.getFlightDetails()));
    }

    public List<Flight> getFlights() { return Collections.unmodifiableList(flights); }
}
