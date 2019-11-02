class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 二维动态规划
        # dp = [[1] * m for _ in range(n)]
        # for i in range(1, n):
        #     for j in range(1, m):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]

        # 一维动态规划
        dp = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j - 1]
        return dp[-1]


print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths(7, 3))
