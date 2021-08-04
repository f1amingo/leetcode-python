#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param n int整型 整数n
# @param k int整型 分为k份
# @return int整型
#
class Solution:
    def divide(self, n, k):
        dp = [[0] * 200 for _ in range(200)]
        dp[0][0] = 1
        dp[1][1] = 1
        dp[1][2] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
        return dp[n][k]


assert Solution().divide(7, 3) == 4
