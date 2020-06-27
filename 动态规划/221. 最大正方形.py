from typing import List
# 反思：
# 1. dp[i][j]不一定需要直接表示最终结果，比如此题求最大正方形的面积，
#    dp[i][j]表示的以(i,j)为右下角的正方形的边长，
#    没有直接和面积挂钩，也不是最大。
# 2. 2维dp画图的时候需要注意，
#    自己总是直接根据dp[i-1][j-1]的图来推dp[i][j]，
#    dp[i-1][j], dp[i][j-1]的信息你不要了吗？

class Solution:
    # my solution
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     if not matrix:
    #         return 0
    #     m = len(matrix)
    #     n = len(matrix[0])
    #     if n == 0:
    #         return 0
    #     dp = [[0] * n for _ in range(m)]
    #     max_edge = 0
    #     for i in range(m):
    #         dp[i][0] = 1 if matrix[i][0] == '1' else 0
    #         max_edge = max(max_edge, dp[i][0])
    #     for j in range(n):
    #         dp[0][j] = 1 if matrix[0][j] == '1' else 0
    #         max_edge = max(max_edge, dp[0][j])
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if matrix[i][j] == '1':
    #                 dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    #                 if dp[i][j] > max_edge:
    #                     max_edge = dp[i][j]
    #     return max_edge * max_edge

    # 官方
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_edge = 0
        # 把判断合并起来
        if not matrix or not len(matrix[0]):
            return max_edge
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    # 主循环中处理边界
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    # 更新最大值的优雅做法
                    max_edge = max(max_edge, dp[i][j])
        return max_edge * max_edge


mat = [
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
]
print(Solution().maximalSquare(mat))
