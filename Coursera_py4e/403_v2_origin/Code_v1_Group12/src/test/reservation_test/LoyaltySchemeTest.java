// test/reservation_test/LoyaltySchemeTest.java
package test.reservation_test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import reservation.LoyaltyScheme;
import reservation.Passenger;

import static org.junit.jupiter.api.Assertions.*;

public class LoyaltySchemeTest {
    private LoyaltyScheme scheme;
    private Passenger passenger;

    @BeforeEach
    void setUp() {
        passenger = new Passenger("P001", "Test Passenger", "test@example.com", "1234567890");
        scheme = new LoyaltyScheme("L001", "Test Scheme", passenger);
    }

    @Test
    void testAccumulateMiles() {
        scheme.accumulateMiles(100);
        assertEquals(100, scheme.getMilesBalance());
    }

    @Test
    void testRedeemMiles() {
        scheme.accumulateMiles(100);
        scheme.redeemMiles(50);
        assertEquals(50, scheme.getMilesBalance());
    }

    @Test
    void testInsufficientMiles() {
        assertThrows(IllegalStateException.class, () ->
                scheme.redeemMiles(100));
    }
}
