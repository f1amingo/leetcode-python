from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = dp[i][max(j - 1, 0)] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[max(i - 1, 0)][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[-1][-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(Solution().minPathSum(grid))
