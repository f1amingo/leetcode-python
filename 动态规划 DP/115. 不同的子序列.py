class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        # s[:i]中含有dp[i][j]个t[:j]子序列
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if i == 0:
                dp[0][0] = 1 if s[i] == t[0] else 0
            else:
                dp[i][0] = dp[i - 1][0]
                if s[i] == t[0]:
                    dp[i][0] += 1
        for i in range(1, m):
            for j in range(1, min(i + 1, n)):
                # s[:i]中包含t[:j]，隐含了s[:i-1]包含t[:j]
                dp[i][j] = dp[i - 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]


assert Solution().numDistinct('rabbbit', 'rabbit') == 3
assert Solution().numDistinct('babgbag', 'bag') == 5
