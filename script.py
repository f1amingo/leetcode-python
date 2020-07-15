from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        res = 0
        for i in range(m):
            tmp = [0] * (n + 1)
            for j in range(1, n + 1):
                if matrix[i][j - 1]:
                    tmp[j] = min(tmp[j - 1], dp[j], dp[j - 1]) + 1
                    res += tmp[j]
            dp = tmp
        return res


print(Solution().countSquares([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))
