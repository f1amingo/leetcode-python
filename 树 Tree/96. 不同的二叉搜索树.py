class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[i - j - 1] * dp[j]
        return dp[-1]


print(Solution().numTrees(1))
