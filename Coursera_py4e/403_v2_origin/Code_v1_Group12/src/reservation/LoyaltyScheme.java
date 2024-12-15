
package reservation;

/**
 * 忠诚计划类
 * 修改说明：
 * 1. 移除了继承关系
 * 2. 使用组合而不是继承
 * 3. 添加了异常处理
 */
public class LoyaltyScheme implements LoyaltyConvertible {
    private final String id;
    private final String schemeName;
    private final Passenger passenger;
    private int miles;

    public LoyaltyScheme(String id, String schemeName, Passenger passenger) {
        if (id == null || id.trim().isEmpty()) {
            throw new IllegalArgumentException("Scheme ID cannot be null or empty");
        }
        if (schemeName == null || schemeName.trim().isEmpty()) {
            throw new IllegalArgumentException("Scheme name cannot be null or empty");
        }
        if (passenger == null) {
            throw new IllegalArgumentException("Passenger cannot be null");
        }

        this.id = id;
        this.schemeName = schemeName;
        this.passenger = passenger;
        this.miles = 0;
    }

    @Override
    public void accumulateMiles(int miles) {
        if (miles <= 0) {
            throw new IllegalArgumentException("Miles must be positive");
        }

        try {
            this.miles += miles;
            passenger.notify(String.format("Added %d miles. New balance: %d", miles, this.miles));
        } catch (Exception e) {
            throw new RuntimeException("Failed to accumulate miles", e);
        }
    }

    @Override
    public void redeemMiles(int miles) {
        if (miles <= 0) {
            throw new IllegalArgumentException("Miles must be positive");
        }
        if (this.miles < miles) {
            throw new IllegalStateException("Insufficient miles for redemption");
        }

        try {
            this.miles -= miles;
            passenger.notify(String.format("Redeemed %d miles. Remaining balance: %d", miles, this.miles));
        } catch (Exception e) {
            throw new RuntimeException("Failed to redeem miles", e);
        }
    }

    @Override
    public int getMilesBalance() {
        return miles;
    }
    public String getId() { return id; }
    public String getSchemeName() { return schemeName; }
}