class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0] * (n + 1)
        dp[2], dp[3] = 2, 3
        for i in range(4, n + 1):
            for j in range(2, i // 2 + 1):
                dp[i] = max(dp[i], dp[i - j] * dp[j])
        return dp[-1]


print(Solution().cuttingRope(10))
