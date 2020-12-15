class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        total = n
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if j - i > 1 else True
                    if dp[i][j]:
                        total += 1
        return total


assert Solution().countSubstrings("fdsklf") == 6
assert Solution().countSubstrings("") == 0
assert Solution().countSubstrings("a") == 1
assert Solution().countSubstrings("abc") == 3
assert Solution().countSubstrings("aaa") == 6
