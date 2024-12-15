// management/InventoryManager.java
package management;

import reservation.Flight;

/**
 * 库存管理器类
 * 修改说明：
 * 1. 删除了继承关系，改用接口实现
 * 2. 使用组合而不是继承
 * 3. 添加了异常处理
 */
public class InventoryManager implements AdminCenter, Reportable {
    private final FlightSchedule schedule;

    public InventoryManager(FlightSchedule schedule) {
        if (schedule == null) {
            throw new IllegalArgumentException("Schedule cannot be null");
        }
        this.schedule = schedule;
    }

    @Override
    public void performManagement() {
        try {
            checkInventory();
        } catch (Exception e) {
            throw new RuntimeException("Failed to perform inventory management", e);
        }
    }

    @Override
    public void generateReport() {
        try {
            System.out.println("\n=== Inventory Report ===");
            schedule.getFlights().forEach(this::generateFlightInventoryReport);
            System.out.println("======================");
        } catch (Exception e) {
            throw new RuntimeException("Failed to generate inventory report", e);
        }
    }

    private void checkInventory() {
        schedule.getFlights().forEach(this::checkFlightInventory);
    }

    private void checkFlightInventory(Flight flight) {
        try {
            System.out.printf("Flight %s - Available seats: %d\n",
                    flight.getFlightNumber(),
                    flight.getCapacity() - flight.getReservations().size());
        } catch (Exception e) {
            throw new RuntimeException("Failed to check flight inventory", e);
        }
    }

    private void generateFlightInventoryReport(Flight flight) {
        try {
            double occupancyRate = flight.calculateOccupancyRate();
            System.out.printf("Flight %s: %.2f%% occupied\n",
                    flight.getFlightNumber(), occupancyRate);
        } catch (Exception e) {
            throw new RuntimeException("Failed to generate flight inventory report", e);
        }
    }
}