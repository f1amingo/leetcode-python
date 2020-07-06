class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # 逆序遍历
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    # 不用边界处理，不会越界
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][-1]


print(Solution().longestPalindromeSubseq("bbbab"))
