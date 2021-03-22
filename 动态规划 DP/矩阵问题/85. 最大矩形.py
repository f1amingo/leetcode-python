from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0
        # (i, j)向左连续1的数量
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[max(i - 1, 0)][j] + 1
                    # 高度为1
                    ans = max(ans, dp[i][j])
                    x, y = i, j
                    width = dp[i][j]
                    # 向上遍历可能的宽度
                    while y >= 0 and matrix[x][y] == '1':
                        width = min(width, dp[x][y])
                        ans = max(ans, (j - y + 1) * width)
                        y -= 1
        return ans


assert Solution().maximalRectangle(
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
) == 6
