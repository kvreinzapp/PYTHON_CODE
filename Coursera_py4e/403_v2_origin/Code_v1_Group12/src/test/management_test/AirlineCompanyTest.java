
package test.management_test;

import management.AirlineCompany;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import reservation.Flight;
import java.time.LocalDateTime;
import java.time.Duration;

import static org.junit.jupiter.api.Assertions.*;


public class AirlineCompanyTest {
    private AirlineCompany airlineCompany;
    private Flight flight;

    @BeforeEach
    void setUp() {
        airlineCompany = new AirlineCompany("AC001", "Test Airline");

        LocalDateTime departure = LocalDateTime.now().plusHours(2);
        flight = new Flight("FL001", "Beijing", "Shanghai",
                departure, departure.plusHours(2), 100);
    }

    @Test
    void testAddFlight() {
        airlineCompany.addFlight(flight);
        assertTrue(airlineCompany.getFlights().contains(flight));
    }

    @Test
    void testCancelFlight() {
        airlineCompany.addFlight(flight);
        airlineCompany.cancelFlight(flight);
        assertFalse(airlineCompany.getFlights().contains(flight));
        assertFalse(flight.isOpen());
    }

    @Test
    void testDelayFlight() {
        airlineCompany.addFlight(flight);
        LocalDateTime originalDeparture = flight.getDepartureTime();

        Duration delay = Duration.ofMinutes(30);
        airlineCompany.delayFlight(flight, delay);

        assertEquals(originalDeparture.plus(delay), flight.getDepartureTime());
    }
}