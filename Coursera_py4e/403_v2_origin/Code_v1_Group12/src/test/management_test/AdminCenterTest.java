package test.management_test;

import management.AdminCenter;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AdminCenterTest {
    // 将 TestAdminCenter 改为内部类，使用 private static
    private static class TestAdminCenter implements AdminCenter {
        @Override
        public void performManagement() {
            System.out.println("Test management performed");
        }
    }

    @Test
    public void testPerformManagement() {
        AdminCenter center = new TestAdminCenter();
        assertDoesNotThrow(center::performManagement);
    }
}