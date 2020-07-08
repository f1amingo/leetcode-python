class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for c in text1:
            tmp = [0] * (n + 1)
            for j in range(1, n + 1):
                if c == text2[j - 1]:
                    tmp[j] = dp[j - 1] + 1
                else:
                    tmp[j] = max(dp[j], tmp[j - 1])
            dp = tmp
        return dp[-1]


print(Solution().longestCommonSubsequence('abcde', 'ace'))
print(Solution().longestCommonSubsequence('abc', 'abc'))
print(Solution().longestCommonSubsequence('abc', 'def'))
