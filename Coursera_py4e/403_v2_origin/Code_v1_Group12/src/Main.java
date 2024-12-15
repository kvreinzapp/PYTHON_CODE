import management.*;
import reservation.*;
import java.time.Duration;
import java.time.LocalDateTime;
import java.util.*;

public class Main {
    private static Scanner scanner = new Scanner(System.in);
    private static AirlineCompany airlineCompany;
    private static FlightSchedule flightSchedule;
    private static InventoryManager inventoryManager;
    private static List<Passenger> passengers = new ArrayList<>();

    public static void main(String[] args) {
        initializeSystem();

        while (true) {
            System.out.println("\n===== Flight Reservation and Management System =====");
            System.out.println("1. Reservation");
            System.out.println("2. Management");
            System.out.println("3. Exit");
            System.out.print("Select an option: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    reservationMenu();
                    break;
                case "2":
                    managementMenu();
                    break;
                case "3":
                    System.out.println("Exiting system. Goodbye!");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid selection. Please try again.");
            }
        }
    }

    private static void initializeSystem() {
        // 初始化航空公司
        airlineCompany = new AirlineCompany("AC001", "China Eastern Airlines");

        // 初始化航班时刻表
        flightSchedule = new FlightSchedule();

        // 初始化库存管理器
        inventoryManager = new InventoryManager(flightSchedule);

        // 添加一些初始航班
        Flight flight1 = new Flight("CE123", "Beijing", "Shanghai",
                LocalDateTime.of(2024, 10, 25, 10, 30),
                LocalDateTime.of(2024, 10, 25, 12, 45),
                200);
        Flight flight2 = new Flight("CE456", "Shanghai", "Guangzhou",
                LocalDateTime.of(2024, 10, 26, 14, 00),
                LocalDateTime.of(2024, 10, 26, 16, 15),
                180);

        airlineCompany.addFlight(flight1);
        airlineCompany.addFlight(flight2);
        flightSchedule.addFlight(flight1);
        flightSchedule.addFlight(flight2);
    }

    private static void reservationMenu() {
        while (true) {
            System.out.println("\n--- Reservation Menu ---");
            System.out.println("1. Make a Reservation");
            System.out.println("2. Cancel a Reservation");
            System.out.println("3. View Available Flights");
            System.out.println("4. Back to Main Menu");
            System.out.print("Select an option: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    makeReservation();
                    break;
                case "2":
                    cancelReservation();
                    break;
                case "3":
                    viewAvailableFlights();
                    break;
                case "4":
                    return;
                default:
                    System.out.println("Invalid selection. Please try again.");
            }
        }
    }

    private static void makeReservation() {
        System.out.print("Enter Passenger ID: ");
        String passengerId = scanner.nextLine();
        System.out.print("Enter Passenger Name: ");
        String passengerName = scanner.nextLine();
        System.out.print("Enter Email: ");
        String email = scanner.nextLine();
        System.out.print("Enter Phone: ");
        String phone = scanner.nextLine();

        Passenger passenger = new Passenger(passengerId, passengerName, email, phone);
        passengers.add(passenger);

        // 显示可用航班
        viewAvailableFlights();

        System.out.print("Enter Flight Number to book: ");
        String flightNumber = scanner.nextLine();

        Flight selectedFlight = findFlight(flightNumber);
        if (selectedFlight == null) {
            System.out.println("Flight not found.");
            return;
        }

        // 选择票务类别
        System.out.println("Select Ticket Category:");
        System.out.println("1. Economy");
        System.out.println("2. Premium Economy");
        System.out.println("3. Business");
        System.out.println("4. First Class");
        System.out.print("Choice: ");
        String categoryChoice = scanner.nextLine();

        TicketCategory category = switch (categoryChoice) {
            case "1" -> TicketCategory.ECONOMY;
            case "2" -> TicketCategory.PREMIUM_ECONOMY;
            case "3" -> TicketCategory.BUSINESS;
            case "4" -> TicketCategory.FIRST;
            default -> {
                System.out.println("Invalid category selected.");
                yield null;
            }
        };

        if (category == null) return;

        // 创建预订
        String reservationId = "R" + System.currentTimeMillis();
        FlightReservation reservation = new FlightReservation(reservationId, passenger, selectedFlight, category);

        // 选择附加服务
        System.out.println("Select Additional Services (enter numbers separated by commas, or '0' for none):");
        System.out.println("1. Extra Baggage ($50)");
        System.out.println("2. Priority Boarding ($30)");
        System.out.print("Choices: ");
        String addonsInput = scanner.nextLine();

        if (!addonsInput.equals("0")) {
            String[] choices = addonsInput.split(",");
            for (String choice : choices) {
                switch (choice.trim()) {
                    case "1" -> reservation.addAddon(new AddonService("Extra Baggage", 50.0, "Additional 20kg baggage"));
                    case "2" -> reservation.addAddon(new AddonService("Priority Boarding", 30.0, "Priority boarding access"));
                }
            }
        }

        // 确认预订
        reservation.makeReservation();
        System.out.println("Reservation completed successfully.");
    }

    private static void cancelReservation() {
        System.out.print("Enter Flight Number: ");
        String flightNumber = scanner.nextLine();
        System.out.print("Enter Passenger ID: ");
        String passengerId = scanner.nextLine();

        Flight flight = findFlight(flightNumber);
        if (flight == null) {
            System.out.println("Flight not found.");
            return;
        }

        // 查找并取消预订
        flight.getReservations().stream()
                .filter(r -> r.getPassenger().getId().equals(passengerId))
                .findFirst()
                .ifPresent(FlightReservation::cancelReservation);
    }

    private static void viewAvailableFlights() {
        System.out.println("\nAvailable Flights:");
        airlineCompany.getFlights().forEach(f -> {
            System.out.printf("Flight %s: %s -> %s, Departure: %s, Arrival: %s\n",
                    f.getFlightNumber(), f.getOrigin(), f.getDestination(),
                    f.getDepartureTime(), f.getArrivalTime());
        });
    }

    private static void managementMenu() {
        while (true) {
            System.out.println("\n--- Management Menu ---");
            System.out.println("1. Add New Flight");
            System.out.println("2. Cancel Flight");
            System.out.println("3. Delay Flight");
            System.out.println("4. View Flight Schedule");
            System.out.println("5. Check Inventory");
            System.out.println("6. Back to Main Menu");
            System.out.print("Select an option: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    addNewFlight();
                    break;
                case "2":
                    cancelFlight();
                    break;
                case "3":
                    delayFlight();
                    break;
                case "4":
                    viewFlightSchedule();
                    break;
                case "5":
                    checkInventory();
                    break;
                case "6":
                    return;
                default:
                    System.out.println("Invalid selection. Please try again.");
            }
        }
    }

    private static void addNewFlight() {
        System.out.print("Enter Flight Number: ");
        String flightNumber = scanner.nextLine();

        System.out.print("Enter Origin: ");
        String origin = scanner.nextLine();

        System.out.print("Enter Destination: ");
        String destination = scanner.nextLine();

        System.out.print("Enter Departure Time (yyyy-MM-ddTHH:mm): ");
        LocalDateTime departureTime = LocalDateTime.parse(scanner.nextLine());

        System.out.print("Enter Arrival Time (yyyy-MM-ddTHH:mm): ");
        LocalDateTime arrivalTime = LocalDateTime.parse(scanner.nextLine());

        System.out.print("Enter Capacity: ");
        int capacity = Integer.parseInt(scanner.nextLine());

        Flight newFlight = new Flight(flightNumber, origin, destination,
                departureTime, arrivalTime, capacity);

        airlineCompany.addFlight(newFlight);
        flightSchedule.addFlight(newFlight);
        System.out.println("New flight added successfully.");
    }

    private static void cancelFlight() {
        System.out.print("Enter Flight Number: ");
        String flightNumber = scanner.nextLine();

        Flight flight = findFlight(flightNumber);
        if (flight != null) {
            airlineCompany.cancelFlight(flight);
            flightSchedule.removeFlight(flight);
            System.out.println("Flight cancelled successfully.");
        } else {
            System.out.println("Flight not found.");
        }
    }

    private static void delayFlight() {
        System.out.print("Enter Flight Number: ");
        String flightNumber = scanner.nextLine();

        System.out.print("Enter delay in minutes: ");
        int minutes = Integer.parseInt(scanner.nextLine());

        Flight flight = findFlight(flightNumber);
        if (flight != null) {
            airlineCompany.delayFlight(flight, Duration.ofMinutes(minutes));
            System.out.println("Flight delayed successfully.");
        } else {
            System.out.println("Flight not found.");
        }
    }

    private static void viewFlightSchedule() {
        System.out.println("\nFlight Schedule:");
        flightSchedule.getFlights().forEach(f -> {
            System.out.printf("Flight %s: %s -> %s, Departure: %s, Arrival: %s\n",
                    f.getFlightNumber(), f.getOrigin(), f.getDestination(),
                    f.getDepartureTime(), f.getArrivalTime());
        });
    }

    private static void checkInventory() {
        inventoryManager.generateReport();
    }

    private static Flight findFlight(String flightNumber) {
        return airlineCompany.getFlights().stream()
                .filter(f -> f.getFlightNumber().equals(flightNumber))
                .findFirst()
                .orElse(null);
    }
}