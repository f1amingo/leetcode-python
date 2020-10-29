from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = mat[i][j]
                elif mat[i][j]:
                    dp[i][j] += dp[i][j - 1] + mat[i][j]
                min_len = dp[i][j]
                for k in range(i, -1, -1):
                    if not dp[k][j]:
                        break
                    min_len = min(min_len, dp[k][j])
                    res += min_len
        return res


A = [[1, 0, 1],
     [1, 1, 0],
     [1, 1, 0]]
print(Solution().numSubmat(A))
