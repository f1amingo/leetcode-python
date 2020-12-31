class Solution:
    # f[i][j]: [i, j]中最长回文子串的长度
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        f = [[0] * n for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
                ans = max(ans, f[i][j])
        return ans


assert Solution().longestPalindromeSubseq('bbbab') == 4
assert Solution().longestPalindromeSubseq('a') == 1
