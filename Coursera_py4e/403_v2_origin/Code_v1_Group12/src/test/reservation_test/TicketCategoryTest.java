// test/reservation_test/TicketCategoryTest.java
package test.reservation_test;

import org.junit.jupiter.api.Test;
import reservation.TicketCategory;

import static org.junit.jupiter.api.Assertions.*;

public class TicketCategoryTest {
    @Test
    void testEnumValues() {
        assertEquals("Economy", TicketCategory.ECONOMY.getDisplayName());
        assertEquals(1.0, TicketCategory.ECONOMY.getPriceMultiplier());
        assertEquals(0, TicketCategory.ECONOMY.getBonusMiles());

        assertEquals("Business", TicketCategory.BUSINESS.getDisplayName());
        assertEquals(1.5, TicketCategory.BUSINESS.getPriceMultiplier());
        assertEquals(50, TicketCategory.BUSINESS.getBonusMiles());
    }
}