from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * (n + 1)
        for i in range(m):
            # 何时需要倒叙，何时不需要，细心体会
            for j in range(1, n + 1):
                dp[j] = max(dp[j], dp[j - 1]) + grid[i][j - 1]
        return dp[-1]


print(Solution().maxValue([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
