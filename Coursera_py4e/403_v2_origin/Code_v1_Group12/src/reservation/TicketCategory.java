
package reservation;

/**
 * 机票类别枚举
 * 修改说明：
 * 1. 从类改为枚举
 * 2. 添加了bonusMiles属性
 * 3. 移除了所有setter方法
 */
public enum TicketCategory {
    ECONOMY("Economy", 1.0, 0),
    PREMIUM_ECONOMY("Premium Economy", 1.2, 25),
    BUSINESS("Business", 1.5, 50),
    FIRST("First", 2.0, 100);

    private final String displayName;
    private final double priceMultiplier;
    private final int bonusMiles;

    TicketCategory(String displayName, double priceMultiplier, int bonusMiles) {
        this.displayName = displayName;
        this.priceMultiplier = priceMultiplier;
        this.bonusMiles = bonusMiles;
    }

    public String getDisplayName() { return displayName; }
    public double getPriceMultiplier() { return priceMultiplier; }
    public int getBonusMiles() { return bonusMiles; }
}
