from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                # 注意初始化
                if i == 0:
                    dp[j] = dp[max(j - 1, 0)] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[max(j - 1, 0)]) + grid[i][j]
        return dp[-1]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
