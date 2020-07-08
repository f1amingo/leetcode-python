class Solution:
    def waysToChange(self, n: int) -> int:
        M = 1000000007
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if i - 1 >= 0:
                dp[i] = 1
            if i - 5 >= 0:
                dp[i] += dp[i - 5]
            if i - 10 >= 0:
                dp[i] += dp[i - 10]
            if i - 25 >= 0:
                dp[i] += dp[i - 25]
            dp[i] %= M
        return dp[-1]


# print(Solution().waysToChange(10))
# print(Solution().waysToChange(5))
print(Solution().waysToChange(61))
