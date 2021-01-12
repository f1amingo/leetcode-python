from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0] * (6 * n + 1) for _ in range(n)]
        for i in range(1, n + 1):
            for j in range(i, 6 * i + 1):
                idx = i - 1
                if idx == 0:
                    dp[idx][j] = 1
                else:
                    for k in range(1, 7):
                        if j - k >= 0:
                            dp[idx][j] += dp[idx - 1][j - k]
        ans = [0.0] * (5 * n + 1)
        all = 6 ** n
        for i in range(n, 6 * n + 1):
            ans[i - n] = dp[-1][i] / all
        return ans


print(Solution().twoSum(1))
