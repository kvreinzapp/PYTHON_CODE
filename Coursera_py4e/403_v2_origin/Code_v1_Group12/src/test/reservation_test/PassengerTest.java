// test/reservation_test/PassengerTest.java
package test.reservation_test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import reservation.Passenger;

import static org.junit.jupiter.api.Assertions.*;

public class PassengerTest {
    private Passenger passenger;

    @BeforeEach
    void setUp() {
        passenger = new Passenger("P001", "Test Passenger", "test@example.com", "1234567890");
    }

    @Test
    void testNotify() {
        assertDoesNotThrow(() -> passenger.notify("Test notification"));
    }

    @Test
    void testConstructorValidation() {
        assertThrows(IllegalArgumentException.class, () ->
                new Passenger("", "Test", "test@example.com", "1234567890"));

        assertThrows(IllegalArgumentException.class, () ->
                new Passenger("P001", "", "test@example.com", "1234567890"));

        assertThrows(IllegalArgumentException.class, () ->
                new Passenger("P001", "Test", "invalid-email", "1234567890"));
    }

    @Test
    void testGetters() {
        assertEquals("P001", passenger.getId());
        assertEquals("Test Passenger", passenger.getName());
        assertEquals("test@example.com", passenger.getEmail());
        assertEquals("1234567890", passenger.getPhone());
    }
}