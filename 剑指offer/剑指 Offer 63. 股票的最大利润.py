from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        # 卖出日固定时，最大利润由之前的最低价决定
        min_price, ans = prices[0], 0
        for i in range(1, n):
            ans = max(ans, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return ans


print(Solution().maxProfit([7, 6, 4, 3, 1]))
