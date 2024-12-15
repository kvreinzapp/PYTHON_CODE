
package reservation;

/**
 * 里程转换接口
 * 修改说明：
 * 1. 添加了getMilesBalance方法
 * 2. 简化了接口设计
 */
public interface LoyaltyConvertible {
    void accumulateMiles(int miles);
    void redeemMiles(int miles);
    int getMilesBalance();
}