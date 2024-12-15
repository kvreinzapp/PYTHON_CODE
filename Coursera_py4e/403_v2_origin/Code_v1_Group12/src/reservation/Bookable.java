
package reservation;

/**
 * 可预订接口
 * 修改说明：
 * 1. 简化了接口方法
 * 2. 移除了冗余的参数
 */
public interface Bookable {
    void makeReservation();
    void cancelReservation();
    void modifyReservation(TicketCategory newCategory);
}