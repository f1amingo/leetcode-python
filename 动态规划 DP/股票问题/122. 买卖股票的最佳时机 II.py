from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        hold, sell = float('-inf'), 0
        for p in prices:
            hold0 = sell - p
            sell0 = hold + p
            sell, hold = max(sell, sell0), max(hold, hold0)
        return sell

    # 动态规划
    # dp[i][0]: 第i天无股，可获得最大利润
    # dp[i][1]: 第i天有股，可获得最大利润
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     dp = [[0] * 2 for _ in range(n)]
    #     dp[0][1] = -prices[0]
    #     for i in range(1, n):
    #         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    #         dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
    #     return dp[-1][0]

    # 对于上升的区段，A[j]-A[i] = (A[j]-A[j-1]) + ... + (A[i+1]-A[i])
    # 无论是一小段，还是连续几段，只要上升都适用
    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = 0
    #     for i in range(1, len(prices)):
    #         tmp = prices[i] - prices[i - 1]
    #         profit += max(0, tmp)
    #     return profit


assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
