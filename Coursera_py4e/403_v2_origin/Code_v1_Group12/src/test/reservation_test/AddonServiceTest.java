// test/reservation_test/AddonServiceTest.java
package test.reservation_test;

import org.junit.jupiter.api.Test;
import reservation.AddonService;

import static org.junit.jupiter.api.Assertions.*;

public class AddonServiceTest {
    @Test
    void testConstructorAndGetters() {
        AddonService addon = new AddonService("Extra Baggage", 50.0, "Additional baggage allowance");

        assertEquals("Extra Baggage", addon.getName());
        assertEquals(50.0, addon.getPrice());
        assertEquals("Additional baggage allowance", addon.getDescription());
    }

    @Test
    void testConstructorValidation() {
        assertThrows(IllegalArgumentException.class, () ->
                new AddonService("", 50.0, "Description"));

        assertThrows(IllegalArgumentException.class, () ->
                new AddonService("Name", -1.0, "Description"));

        assertThrows(IllegalArgumentException.class, () ->
                new AddonService("Name", 50.0, ""));
    }
}