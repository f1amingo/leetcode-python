from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        if not len(matrix) or not len(matrix[0]):
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                elif matrix[i][j] == '1':
                    pre_i = max(i - 1, 0)
                    pre_j = max(j - 1, 0)
                    dp[i][j] = min(dp[pre_i][j], dp[i][pre_j], dp[pre_i][pre_j]) + 1
                res = max(res, dp[i][j])
        return res * res


mat = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '0'],
]
print(Solution().maximalSquare(mat))
