from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b, c, d = float('-inf'), 0, float('-inf'), 0
        for p in prices:
            a0 = max(a, -p)
            b0 = max(b, a + p)
            c0 = max(c, b - p)
            d0 = max(d, c + p)
            a, b, c, d = a0, b0, c0, d0
        return d


assert Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert Solution().maxProfit([0, 5]) == 5
