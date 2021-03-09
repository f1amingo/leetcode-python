from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b = 0, float('inf')
        for p in prices:
            a = max(a, p - b)
            b = min(b, p)
        return a


assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
