
package reservation;

import java.util.*;

/**
 * 航班预订类
 * 修改说明：
 * 1. 移除了继承关系
 * 2. 使用组合而不是继承
 * 3. 简化了方法参数
 * 4. 添加了业务逻辑验证
 */
public class FlightReservation implements Bookable {
    private final String reservationId;
    private final Passenger passenger;
    private final Flight flight;
    private TicketCategory category;
    private final List<AddonService> addons;

    public FlightReservation(String reservationId, Passenger passenger,
                             Flight flight, TicketCategory category) {
        if (reservationId == null || reservationId.trim().isEmpty()) {
            throw new IllegalArgumentException("Reservation ID cannot be null or empty");
        }
        if (passenger == null) {
            throw new IllegalArgumentException("Passenger cannot be null");
        }
        if (flight == null) {
            throw new IllegalArgumentException("Flight cannot be null");
        }
        if (category == null) {
            throw new IllegalArgumentException("Ticket category cannot be null");
        }

        this.reservationId = reservationId;
        this.passenger = passenger;
        this.flight = flight;
        this.category = category;
        this.addons = new ArrayList<>();
    }

    @Override
    public void makeReservation() {
        try {
            flight.addReservation(this);
        } catch (Exception e) {
            throw new RuntimeException("Failed to make reservation", e);
        }
    }

    @Override
    public void cancelReservation() {
        try {
            flight.removeReservation(this);
        } catch (Exception e) {
            throw new RuntimeException("Failed to cancel reservation", e);
        }
    }

    @Override
    public void modifyReservation(TicketCategory newCategory) {
        if (newCategory == null) {
            throw new IllegalArgumentException("New ticket category cannot be null");
        }

        try {
            this.category = newCategory;
            notify("Ticket category changed to " + newCategory.getDisplayName());
        } catch (Exception e) {
            throw new RuntimeException("Failed to modify reservation", e);
        }
    }

    public void addAddon(AddonService addon) {
        if (addon == null) {
            throw new IllegalArgumentException("Addon service cannot be null");
        }

        try {
            addons.add(addon);
            notify("Added service: " + addon.getName());
        } catch (Exception e) {
            throw new RuntimeException("Failed to add addon service", e);
        }
    }

    public void notify(String message) {
        if (message == null || message.trim().isEmpty()) {
            throw new IllegalArgumentException("Notification message cannot be null or empty");
        }

        try {
            passenger.notify(message);
        } catch (Exception e) {
            throw new RuntimeException("Failed to send notification", e);
        }
    }

    /*
    public void confirm() {

        System.out.println("Reservation " + reservationId + " confirmed.");
    }

    public void cancel() {

        System.out.println("Reservation " + reservationId + " cancelled.");
    }
    */
    //public String getReservationId() { return reservationId; }
    public Passenger getPassenger() { return passenger; }
    public Flight getFlight() { return flight; }
    public TicketCategory getCategory() { return category; }
    public List<AddonService> getAddons() { return Collections.unmodifiableList(addons); }
}