from typing import List


#
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        C = total // 2
        dp = [0] * (C + 1)
        for stone in stones:
            for i in range(C, stone - 1, -1):
                dp[i] = max(dp[i], dp[i - stone] + stone)
        return abs(total - 2 * dp[-1])


assert Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1
