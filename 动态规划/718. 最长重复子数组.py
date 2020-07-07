from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        m, n = len(A), len(B)
        dp = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n, 0, -1):
                if A[i] == B[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
        return res


A = [1, 0, 0, 0, 1]
B = [1, 0, 0, 1, 1]
print(Solution().findLength(A, B))
