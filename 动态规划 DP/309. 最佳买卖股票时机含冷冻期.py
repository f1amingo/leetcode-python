from typing import List


class Solution:
    # 思考第i天能获得的最大利润，可能有三种情况持股，不持股当天卖出（i+1天不可买入），不持股之前卖出
    # dp[i][0]：第i天持股能获得的最大收益
    # dp[i][1]：第i天不持股，并且(i+1)处于冷冻期
    # dp[i][2]：第i天不持股，并且(i+1)不处于冷冻期
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[-1][1], dp[-1][2])


assert Solution().maxProfit([]) == 0
assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3
