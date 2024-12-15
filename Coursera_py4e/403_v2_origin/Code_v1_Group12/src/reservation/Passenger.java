
package reservation;

/**
 * 乘客类
 * 修改说明：
 * 1. 新建类替代PassengerCenter
 * 2. 使用final字段
 * 3. 添加了通知功能
 */
public class Passenger {
    private final String id;
    private final String name;
    private final String email;
    private final String phone;

    public Passenger(String id, String name, String email, String phone) {
        if (id == null || id.trim().isEmpty()) {
            throw new IllegalArgumentException("Passenger ID cannot be null or empty");
        }
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be null or empty");
        }
        if (email == null || !email.contains("@")) {
            throw new IllegalArgumentException("Invalid email address");
        }
        if (phone == null || phone.trim().isEmpty()) {
            throw new IllegalArgumentException("Phone number cannot be null or empty");
        }

        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
    }

    public void notify(String message) {
        if (message == null || message.trim().isEmpty()) {
            throw new IllegalArgumentException("Notification message cannot be null or empty");
        }

        try {
            // 实际实现可能会发送邮件或短信
            System.out.println("Notification to " + name + " (" + email + "): " + message);
        } catch (Exception e) {
            throw new RuntimeException("Failed to send notification", e);
        }
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }
    public String getPhone() { return phone; }
}