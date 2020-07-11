class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(m):
            tmp = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i] == text2[j - 1]:
                    tmp[j] = dp[j - 1] + 1
                else:
                    tmp[j] = max(tmp[j - 1], dp[j])
            dp = tmp
        return dp[-1]


print(Solution().longestCommonSubsequence('abcde', 'a'))
