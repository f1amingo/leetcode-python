from typing import List


class Solution:
    # 如果在第i天卖出，那么最大利润一定是在[0,i-1]之间的最低点买入
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        minVal = float('inf')
        for price in prices:
            minVal = min(minVal, price)
            maxVal = max(maxVal, price - minVal)
        return maxVal

    # 单调队列
    # 要比较当前值和之前的最小值
    # def maxProfit(self, prices: List[int]) -> int:
    #     stk = []
    #     maxVal = 0
    #     for price in prices:
    #         while stk and stk[-1] > price:
    #             stk.pop()
    #         stk.append(price)
    #         maxVal = max(maxVal, stk[-1] - stk[0])
    #     return maxVal

    # 暴力，TLE
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     maxVal = 0
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             maxVal = max(maxVal, prices[j] - prices[i])
    #     return maxVal


assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
