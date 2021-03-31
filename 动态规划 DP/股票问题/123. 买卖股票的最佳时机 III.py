from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s1, s2, s3, s4 = float('-inf'), 0, float('-inf'), 0
        for p in prices:
            s1 = max(s1, -p)
            s2 = max(s2, s1 + p)
            s3 = max(s3, s2 - p)
            s4 = max(s4, s3 + p)
        return max(0, s4)


assert Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
