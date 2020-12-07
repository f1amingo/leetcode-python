from typing import List


class Solution:
    # wrong
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        m, n = G, len(profit)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        total = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i][j - 1], profit[j - 1] + dp[max(i - group[i - 1], 0)][j - 1])
                if dp[i][j] >= P:
                    total += 1
        return total % 1000000007


assert Solution().profitableSchemes(5, 3, [2, 2], [2, 3]) == 2
assert Solution().profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 7
