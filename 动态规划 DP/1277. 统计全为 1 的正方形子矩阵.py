from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # 关键点：dp[i][j]与以(i, j)为右下角的正方形的数目相同
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j]:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                res += dp[i][j]
        return res

    # 滚动数组
    # def countSquares(self, matrix: List[List[int]]) -> int:
    #     if not matrix or not matrix[0]:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #     dp = [0] * (n + 1)
    #     res = 0
    #     for i in range(m):
    #         tmp = [0] * (n + 1)
    #         for j in range(1, n + 1):
    #             if matrix[i][j - 1]:
    #                 tmp[j] = min(tmp[j - 1], dp[j], dp[j - 1]) + 1
    #                 res += tmp[j]
    #         dp = tmp
    #     return res


print(Solution().countSquares([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))

print(Solution().countSquares([
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))
