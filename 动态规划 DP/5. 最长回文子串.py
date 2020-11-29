class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        start, end = 0, 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, n):
                if j - i == 1:
                    dp[i][j] = s[i] == s[j]
                elif j - i > 1:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j] and j - i > end - start:
                    start, end = i, j
        return s[start:end + 1]


assert Solution().longestPalindrome("babad") == 'bab' or Solution().longestPalindrome("babad") == 'aba'
assert Solution().longestPalindrome("cbbd") == 'bb'
