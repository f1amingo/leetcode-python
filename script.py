class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        lt, rt = 0, 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = j - i < 3 or dp[i + 1][j - 1]
                if dp[i][j] and j - i > rt - lt:
                    lt, rt = i, j
        return s[lt:rt + 1]


print(Solution().longestPalindrome('cbbd'))
print(Solution().longestPalindrome('babad'))
