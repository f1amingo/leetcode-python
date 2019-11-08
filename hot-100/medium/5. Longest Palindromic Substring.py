class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        start = end = 0
        max_len = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = j - i <= 2 or dp[i + 1][j - 1]
                cur_len = j - i + 1
                if dp[i][j] and cur_len > max_len:
                    max_len = cur_len
                    start = i
                    end = j
        return s[start:end + 1]


print(Solution().longestPalindrome("aaaa"))
