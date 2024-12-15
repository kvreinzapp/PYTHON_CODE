// test/management_test/FlightScheduleTest.java
package test.management_test;

import management.FlightSchedule;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import reservation.Flight;
import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

public class FlightScheduleTest {
    private FlightSchedule schedule;
    private Flight flight;

    @BeforeEach
    void setUp() {
        schedule = new FlightSchedule();

        LocalDateTime departure = LocalDateTime.now().plusHours(2);
        flight = new Flight("FL001", "Beijing", "Shanghai",
                departure, departure.plusHours(2), 100);
    }

    @Test
    void testAddFlight() {
        schedule.addFlight(flight);
        assertTrue(schedule.getFlights().contains(flight));
    }

    @Test
    void testRemoveFlight() {
        schedule.addFlight(flight);
        schedule.removeFlight(flight);
        assertFalse(schedule.getFlights().contains(flight));
    }
}
