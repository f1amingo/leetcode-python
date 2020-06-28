from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        dp = [0] * n
        for i in range(n):
            for j in range(i, -1, -1):
                dp[j] = min(dp[min(j, i - 1)], dp[max(j - 1, 0)]) + triangle[i][j]
        return min(dp)


tri = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(Solution().minimumTotal(tri))
