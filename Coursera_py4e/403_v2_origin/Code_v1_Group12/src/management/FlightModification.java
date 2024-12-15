
package management;

import reservation.Flight;

/**
 * 航班修改类
 * 修改说明：
 * 1. 删除了继承关系，改用接口实现
 * 2. 使用组合而不是继承
 * 3. 添加了异常处理
 */
public class FlightModification implements AdminCenter {
    private final Flight flight;
    private final String modificationDetails;

    public FlightModification(Flight flight, String modificationDetails) {
        if (flight == null) {
            throw new IllegalArgumentException("Flight cannot be null");
        }
        if (modificationDetails == null || modificationDetails.trim().isEmpty()) {
            throw new IllegalArgumentException("Modification details cannot be null or empty");
        }

        this.flight = flight;
        this.modificationDetails = modificationDetails;
    }

    @Override
    public void performManagement() {
        try {
            applyModification();
            notifyPassengers();
        } catch (Exception e) {
            throw new RuntimeException("Failed to perform flight modification", e);
        }
    }

    private void applyModification() {
        try {
            System.out.println("Applied modification: " + modificationDetails);
        } catch (Exception e) {
            throw new RuntimeException("Failed to apply modification", e);
        }
    }

    private void notifyPassengers() {
        try {
            flight.notifyAllPassengers("Flight modification: " + modificationDetails);
        } catch (Exception e) {
            throw new RuntimeException("Failed to notify passengers", e);
        }
    }

    public Flight getFlight() { return flight; }
    public String getModificationDetails() { return modificationDetails; }
}
