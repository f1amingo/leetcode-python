class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


assert Solution().numTrees(1) == 1
assert Solution().numTrees(2) == 2
assert Solution().numTrees(3) == 5
