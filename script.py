from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            m = len(triangle[i])
            for j in range(m):
                if i == n - 1:
                    dp[j] = triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


print(Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
