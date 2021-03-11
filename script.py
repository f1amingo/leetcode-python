from typing import List


class Solution:
    def comb(self, n: int, k: int) -> int:
        dp = [0] * (k + 1)

        dp = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            for j in range(k + 1):
                for p in range(j + 1):
                    dp[i][j] += dp[i][]
        return dp[-1][-1]


print(Solution().maxProfit(2, [2, 4, 1]))
