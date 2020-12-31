# 回文子串，连续
# dp[i][j]：是否是回文子串
# dp[i][j] -> dp[i+1][j-1]
class Solution:
    # 中心扩散
    def longestPalindrome(self, s: str) -> str:
        def dfs(i: int, j: int):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            i, j = i + 1, j - 1
            nonlocal lt, rt
            if j - i > rt - lt:
                lt, rt = i, j

        n = len(s)
        lt, rt = 0, 0
        for i in range(n - 1):
            dfs(i, i)
            dfs(i, i + 1)
        return s[lt:rt + 1]

    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     lt, rt = 0, 0
    #     dp = [[False] * n for _ in range(n)]
    #     for i in range(n - 1, -1, -1):
    #         dp[i][i] = True
    #         for j in range(i + 1, n):
    #             if s[i] == s[j]:
    #                 dp[i][j] = True if j - i <= 1 else dp[i + 1][j - 1]
    #             if dp[i][j] and j - i > rt - lt:
    #                 lt, rt = i, j
    #     return s[lt:rt + 1]


assert Solution().longestPalindrome('babad') == 'bab'
assert Solution().longestPalindrome('cbbd') == 'bb'
assert Solution().longestPalindrome('a') == 'a'
assert Solution().longestPalindrome('') == ''
