from typing import List


class Solution:

    # 动态规划
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # 两个数及以下，先手必赢
        if n < 3:
            return True
        # dp[i][j]: 先手从[i, j]区间内赢得的分数
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0

    # 记忆化递归
    # def PredictTheWinner(self, nums: List[int]) -> bool:
    #     # [i, j]区间内可以获得的最大分数
    #     def helper(i: int, j: int) -> int:
    #         if i == j:
    #             return nums[i]
    #         if memo[i][j] is None:
    #             # 选择nums[i]，输掉helper(i+1, j)分
    #             pickI = nums[i] - helper(i + 1, j)
    #             pickJ = nums[j] - helper(i, j - 1)
    #             memo[i][j] = max(pickI, pickJ)
    #         return memo[i][j]
    #
    #     n = len(nums)
    #     if n < 2:
    #         return True
    #     memo = [[None] * n for _ in range(n)]
    #     return helper(0, len(nums) - 1) >= 0

    # 无记忆递归
    # def PredictTheWinner(self, nums: List[int]) -> bool:
    #     # [i, j]区间内可以获得的最大分数
    #     def helper(i: int, j: int) -> int:
    #         if i == j:
    #             return nums[i]
    #         # 选择nums[i]，输掉helper(i+1, j)分
    #         pickI = nums[i] - helper(i + 1, j)
    #         pickJ = nums[j] - helper(i, j - 1)
    #         return max(pickI, pickJ)
    #
    #     return nums and helper(0, len(nums) - 1) >= 0


print(Solution().PredictTheWinner([1, 5, 2]))
print(Solution().PredictTheWinner([1, 5, 233, 7]))
