from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A or not len(A) or not len(A[0]):
            return 0
        m, n = len(A), len(A[0])
        dp = [[0] * n for _ in range(m)]
        res = float('inf')
        for i in range(m):
            for j in range(n):
                # 但出现这种写法时，可以选择只有一行的测试用例
                if i == 0:
                    dp[i][j] = A[i][j]
                else:
                    # 边界处理可以max(0,j-1)
                    left = dp[i - 1][j - 1] if j - 1 >= 0 else float('inf')
                    right = dp[i - 1][j + 1] if j + 1 < n else float('inf')
                    dp[i][j] = min(dp[i - 1][j], left, right) + A[i][j]
                if i == m - 1:
                    res = min(res, dp[i][j])
        return res


print(Solution().minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().minFallingPathSum([[69]]))
print(Solution().minFallingPathSum([[3, 2, 1]]))
