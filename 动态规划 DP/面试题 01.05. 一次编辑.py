class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if not first and not second:
            return True
        m, n = len(first), len(second)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if first[i - 1] == second[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[-1][-1] <= 1


print(Solution().oneEditAway("a", "a"))
print(Solution().oneEditAway("", ""))
print(Solution().oneEditAway("pale", "ple"))
print(Solution().oneEditAway("pales", "pal"))
