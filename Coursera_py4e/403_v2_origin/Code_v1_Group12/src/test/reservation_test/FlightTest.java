// test/reservation_test/FlightTest.java
package test.reservation_test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import reservation.*;
import java.time.LocalDateTime;
import java.time.Duration;

import static org.junit.jupiter.api.Assertions.*;

public class FlightTest {
    private Flight flight;
    private Passenger passenger;
    private FlightReservation reservation;

    @BeforeEach
    void setUp() {
        LocalDateTime departure = LocalDateTime.now().plusHours(2);
        flight = new Flight("FL001", "Beijing", "Shanghai",
                departure, departure.plusHours(2), 2);

        passenger = new Passenger("P001", "Test Passenger", "test@example.com", "1234567890");
        reservation = new FlightReservation("R001", passenger, flight, TicketCategory.ECONOMY);
    }

    @Test
    void testAddReservation() {
        flight.addReservation(reservation);
        assertTrue(flight.getReservations().contains(reservation));
    }

    @Test
    void testRemoveReservation() {
        flight.addReservation(reservation);
        flight.removeReservation(reservation);
        assertFalse(flight.getReservations().contains(reservation));
    }

    @Test
    void testDelay() {
        LocalDateTime originalDeparture = flight.getDepartureTime();
        Duration delay = Duration.ofMinutes(30);
        flight.delay(delay);
        assertEquals(originalDeparture.plus(delay), flight.getDepartureTime());
    }

    @Test
    void testCancel() {
        flight.cancel();
        assertFalse(flight.isOpen());
    }
}