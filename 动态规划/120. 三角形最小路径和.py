from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 自顶向下
        # if not triangle:
        #     return 0
        # n = len(triangle)
        # dp = [0] * n
        # for i in range(n):
        #     for j in range(i, -1, -1):
        #         dp[j] = min(dp[min(j, i - 1)], dp[max(j - 1, 0)]) + triangle[i][j]
        # return min(dp)

        # 自底向上
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


tri = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(Solution().minimumTotal(tri))
