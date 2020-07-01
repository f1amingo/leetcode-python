from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])
        if not n:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 or dp[i - 1][0] == 0 else 1
        for i in range(1, n):
            dp[0][i] = 0 if obstacleGrid[0][i] == 1 or dp[0][i - 1] == 0 else 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    if obstacleGrid[i - 1][j] == 0:
                        dp[i][j] += dp[i - 1][j]
                    if obstacleGrid[i][j - 1] == 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]


grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))
