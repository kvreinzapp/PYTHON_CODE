// test/management_test/InventoryManagerTest.java
package test.management_test;

import management.FlightSchedule;
import management.InventoryManager;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import reservation.*;
import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;


public class InventoryManagerTest {
    private FlightSchedule schedule;
    private InventoryManager inventory;
    private Flight flight;

    @BeforeEach
    void setUp() {
        schedule = new FlightSchedule();
        inventory = new InventoryManager(schedule);

        LocalDateTime departure = LocalDateTime.now().plusHours(2);
        flight = new Flight("FL001", "Beijing", "Shanghai",
                departure, departure.plusHours(2), 100);

        schedule.addFlight(flight);
    }

    @Test
    void testGenerateReport() {
        assertDoesNotThrow(() -> inventory.generateReport());
    }

    @Test
    void testPerformManagement() {
        assertDoesNotThrow(() -> inventory.performManagement());
    }
}