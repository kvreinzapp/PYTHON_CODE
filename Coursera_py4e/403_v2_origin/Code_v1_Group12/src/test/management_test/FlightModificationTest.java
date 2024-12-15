package test.management_test;

import management.FlightModification;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import reservation.Flight;
import java.time.LocalDateTime;

/**
 * FlightModificationTest
 * 修改说明：
 * 1. 更新了构造函数调用以匹配新的FlightModification类结构
 * 2. 更新了Flight的构造函数调用
 * 3. 添加了必要的断言
 * 4. 移除了已不存在的方法的测试
 */
public class FlightModificationTest {
    private FlightModification flightModification;
    private Flight flight;

    @BeforeEach
    void setUp() {
        // 更新Flight构造函数调用，移除了不需要的参数
        flight = new Flight(
                "TM456",
                "Paris",
                "Berlin",
                LocalDateTime.now().plusHours(3),
                LocalDateTime.now().plusHours(5),
                100
        );

        // 更新FlightModification构造函数调用，只需要flight和修改详情
        flightModification = new FlightModification(
                flight,
                "Change aircraft type"
        );
    }

    @Test
    void testPerformManagement() {
        // 测试performManagement方法的执行
        assertDoesNotThrow(() -> flightModification.performManagement());
    }

    @Test
    void testGetters() {
        // 测试getter方法
        assertEquals(flight, flightModification.getFlight());
        assertEquals("Change aircraft type", flightModification.getModificationDetails());
    }

    @Test
    void testConstructorValidation() {
        // 测试构造函数参数验证
        assertThrows(IllegalArgumentException.class, () ->
                new FlightModification(null, "Change aircraft type"));

        assertThrows(IllegalArgumentException.class, () ->
                new FlightModification(flight, null));

        assertThrows(IllegalArgumentException.class, () ->
                new FlightModification(flight, ""));
    }
}