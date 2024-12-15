package reservation;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.*;

/**
 * 航班类
 * 修改说明：
 * 1. 删除了继承自PassengerCenter的设计
 * 2. 删除了所有setter方法，改用业务方法如delay()
 * 3. 移除了Notifiable接口，改用直接的notify方法
 * 4. 添加了异常处理
 */
public class Flight {
    private final String flightNumber;
    private final String origin;
    private final String destination;
    private LocalDateTime departureTime;
    private LocalDateTime arrivalTime;
    private final int capacity;
    private final List<FlightReservation> reservations;
    private boolean isOpen;

    public Flight(String flightNumber, String origin, String destination,
                  LocalDateTime departureTime, LocalDateTime arrivalTime, int capacity) {
        // 参数验证
        if (flightNumber == null || origin == null || destination == null ||
                departureTime == null || arrivalTime == null) {
            throw new IllegalArgumentException("Flight parameters cannot be null");
        }
        if (capacity <= 0) {
            throw new IllegalArgumentException("Capacity must be positive");
        }
        if (arrivalTime.isBefore(departureTime)) {
            throw new IllegalArgumentException("Arrival time cannot be before departure time");
        }

        this.flightNumber = flightNumber;
        this.origin = origin;
        this.destination = destination;
        this.departureTime = departureTime;
        this.arrivalTime = arrivalTime;
        this.capacity = capacity;
        this.reservations = new ArrayList<>();
        this.isOpen = true;
    }

    /**
     * 延迟航班
     * 修改说明：替代了原来的setDepartureTime和setArrivalTime方法
     */
    public void delay(Duration delay) {
        if (delay == null) {
            throw new IllegalArgumentException("Delay duration cannot be null");
        }
        if (delay.isNegative()) {
            throw new IllegalArgumentException("Delay duration cannot be negative");
        }

        try {
            this.departureTime = departureTime.plus(delay);
            this.arrivalTime = arrivalTime.plus(delay);
            notifyAllPassengers("Flight " + flightNumber + " has been delayed by " + delay.toMinutes() + " minutes");
        } catch (Exception e) {
            throw new RuntimeException("Failed to process flight delay", e);
        }
    }

    /**
     * 取消航班
     * 修改说明：新增方法，替代直接修改isOpen字段
     */
    public void cancel() {
        if (!isOpen) {
            throw new IllegalStateException("Flight is already cancelled");
        }

        try {
            this.isOpen = false;
            notifyAllPassengers("Flight " + flightNumber + " has been cancelled");
        } catch (Exception e) {
            throw new RuntimeException("Failed to cancel flight", e);
        }
    }

    /**
     * 添加预订
     * 修改说明：新增方法，替代直接操作reservations列表
     */
    public void addReservation(FlightReservation reservation) {
        if (reservation == null) {
            throw new IllegalArgumentException("Reservation cannot be null");
        }
        if (!isOpen) {
            throw new IllegalStateException("Cannot add reservation to closed flight");
        }
        if (isFull()) {
            throw new IllegalStateException("Flight is full");
        }

        try {
            reservations.add(reservation);
            reservation.notify("Successfully booked on flight " + flightNumber);
        } catch (Exception e) {
            throw new RuntimeException("Failed to add reservation", e);
        }
    }

    /**
     * 移除预订
     * 修改说明：新增方法，替代直接操作reservations列表
     */
    public void removeReservation(FlightReservation reservation) {
        if (reservation == null) {
            throw new IllegalArgumentException("Reservation cannot be null");
        }

        try {
            if (reservations.remove(reservation)) {
                reservation.notify("Removed from flight " + flightNumber);
            } else {
                throw new IllegalArgumentException("Reservation not found");
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to remove reservation", e);
        }
    }

    /**
     * 通知所有乘客
     * 修改说明：替代了Notifiable接口的实现
     */
    public void notifyAllPassengers(String message) {
        if (message == null || message.trim().isEmpty()) {
            throw new IllegalArgumentException("Notification message cannot be empty");
        }

        try {
            reservations.forEach(reservation -> reservation.notify(message));
        } catch (Exception e) {
            throw new RuntimeException("Failed to notify passengers", e);
        }
    }

    public boolean isFull() {
        return reservations.size() >= capacity;
    }

    public double calculateOccupancyRate() {
        return (double) reservations.size() / capacity * 100;
    }

    public String getFlightDetails() {
        return String.format("Flight %s: %s -> %s, Departure: %s, Arrival: %s, Occupancy: %.1f%%",
                flightNumber, origin, destination, departureTime, arrivalTime, calculateOccupancyRate());
    }

    // Getters - 不可变字段的安全访问
    public String getFlightNumber() { return flightNumber; }
    public String getOrigin() { return origin; }
    public String getDestination() { return destination; }
    public LocalDateTime getDepartureTime() { return departureTime; }
    public LocalDateTime getArrivalTime() { return arrivalTime; }
    public int getCapacity() { return capacity; }
    public List<FlightReservation> getReservations() {
        return Collections.unmodifiableList(reservations);
    }
    public boolean isOpen() { return isOpen; }
}