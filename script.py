from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = [0] * n
        for i in range(m):
            tmp = [0] * n
            for j in range(n):
                if i == 0:
                    tmp[j] = A[i][j]
                else:
                    tmp[j] = min(dp[j], dp[max(0, j - 1)], dp[min(n - 1, j + 1)]) + A[i][j]
            dp = tmp
        return min(dp)


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = [[-19, 57], [-40, -5]]
print(Solution().minFallingPathSum(A))
