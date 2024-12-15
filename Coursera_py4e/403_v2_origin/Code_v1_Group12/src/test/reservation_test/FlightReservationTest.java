// test/reservation_test/FlightReservationTest.java
package test.reservation_test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import reservation.*;
import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

public class FlightReservationTest {
    private Flight flight;
    private Passenger passenger;
    private FlightReservation reservation;

    @BeforeEach
    void setUp() {
        LocalDateTime departure = LocalDateTime.now().plusHours(2);
        flight = new Flight("FL001", "Beijing", "Shanghai",
                departure, departure.plusHours(2), 100);

        passenger = new Passenger("P001", "Test Passenger", "test@example.com", "1234567890");
        reservation = new FlightReservation("R001", passenger, flight, TicketCategory.ECONOMY);
    }

    @Test
    void testMakeReservation() {
        reservation.makeReservation();
        assertTrue(flight.getReservations().contains(reservation));
    }

    @Test
    void testCancelReservation() {
        reservation.makeReservation();
        reservation.cancelReservation();
        assertFalse(flight.getReservations().contains(reservation));
    }

    @Test
    void testModifyReservation() {
        reservation.modifyReservation(TicketCategory.BUSINESS);
        assertEquals(TicketCategory.BUSINESS, reservation.getCategory());
    }

    @Test
    void testAddAddon() {
        AddonService addon = new AddonService("Extra Baggage", 50.0, "Additional baggage allowance");
        reservation.addAddon(addon);
        assertTrue(reservation.getAddons().contains(addon));
    }
}
