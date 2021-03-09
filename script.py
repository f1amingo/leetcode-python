from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sell = float('-inf'), 0
        for p in prices:
            hold0 = sell - p
            sell0 = hold + p
            sell, hold = max(sell, sell0), max(hold, hold0)
        return sell


assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
