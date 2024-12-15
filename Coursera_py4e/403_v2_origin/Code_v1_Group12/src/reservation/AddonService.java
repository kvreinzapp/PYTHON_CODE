
package reservation;

/**
 * 附加服务类
 * 修改说明：
 * 1. 重命名自OptionalAddon
 * 2. 移除了继承关系
 * 3. 添加了final字段
 */
public class AddonService {
    private final String name;
    private final double price;
    private final String description;

    public AddonService(String name, double price, String description) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Service name cannot be null or empty");
        }
        if (price < 0) {
            throw new IllegalArgumentException("Price cannot be negative");
        }
        if (description == null || description.trim().isEmpty()) {
            throw new IllegalArgumentException("Description cannot be null or empty");
        }

        this.name = name;
        this.price = price;
        this.description = description;
    }

    public String getName() { return name; }
    public double getPrice() { return price; }
    public String getDescription() { return description; }
}