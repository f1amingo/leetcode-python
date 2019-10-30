class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_count = len(grid)
        col_count = len(grid[0])
        dp = [[0] * col_count] * row_count
        for i in range(row_count - 1, -1, -1):
            for j in range(col_count - 1, -1, -1):
                if j == col_count - 1 and i == row_count - 1:
                    dp[i][j] = grid[i][j]
                elif j == col_count - 1:
                    # 右边界
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif i == row_count - 1:
                    # 左边界
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(Solution().minPathSum(grid))
