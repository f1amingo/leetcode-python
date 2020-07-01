class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if not n or not m:
            return 0
        if n == m:
            return 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1:
                    dp[i][j] = j
                    continue
                if j == 1:
                    dp[i][j] = i
                    continue
                if i > j:
                    dp[i][j] = dp[i - j][j] + 1
                elif j > i:
                    dp[i][j] = dp[i][j - i] + 1
                else:
                    dp[i][j] = 1
        return dp[-1][-1]


print(Solution().tilingRectangle(1, 1))
print(Solution().tilingRectangle(2, 3))
print(Solution().tilingRectangle(0, 3))
print(Solution().tilingRectangle(5, 8))
print(Solution().tilingRectangle(11, 13))

