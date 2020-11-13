from typing import List


class Solution:
    # 动态规划
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        if n < 4:
            return True
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = piles[i]
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[-1][-1] > 0

    # 记忆化递归
    # def stoneGame(self, piles: List[int]) -> bool:
    #     n = len(piles)
    #     if n < 4:
    #         return True
    #     memo = [[None] * n for _ in range(n)]
    #
    #     # [i,j]区间内赢过对方的最大分数
    #     def dfs(i: int, j: int) -> int:
    #         if i > j:
    #             return 0
    #         if not memo[i][j]:
    #             if j == i:
    #                 memo[i][j] = piles[i]
    #             else:
    #                 pickI = piles[i] - dfs(i + 1, j)
    #                 pickJ = piles[j] - dfs(i, j - 1)
    #                 memo[i][j] = max(pickI, pickJ)
    #         return memo[i][j]
    #
    #     return dfs(0, len(piles) - 1) > 0

    # 递归，超时
    # def stoneGame(self, piles: List[int]) -> bool:
    #     n = len(piles)
    #     if n < 4:
    #         return True
    #
    #     # [i,j]区间内赢过对方的最大分数
    #     def dfs(i: int, j: int) -> int:
    #         if i > j:
    #             return 0
    #         if j == i:
    #             return piles[i]
    #         pickI = piles[i] - dfs(i + 1, j)
    #         pickJ = piles[j] - dfs(i, j - 1)
    #         return max(pickI, pickJ)
    #
    #     return dfs(0, len(piles) - 1) > 0


print(Solution().stoneGame(
    [7, 7, 12, 16, 41, 48, 41, 48, 11, 9, 34, 2, 44, 30, 27, 12, 11, 39, 31, 8, 23, 11, 47, 25, 15, 23, 4, 17, 11, 50,
     16, 50, 38, 34, 48, 27, 16, 24, 22, 48, 50, 10, 26, 27, 9, 43, 13, 42, 46, 24]))
print(Solution().stoneGame([5, 3, 4, 5]))
