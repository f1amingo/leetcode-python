from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        _sum = sum(stones)
        half_sum = _sum // 2
        dp = [0] * (half_sum + 1)
        for stone in stones:
            for j in range(half_sum, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        return _sum - 2 * dp[-1]


print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]))
