from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dfs遍历所有情况
        # 超时
        # if not nums:
        #     return True
        # n = len(nums)
        #
        # def dfs(_next):
        #     if _next == n - 1:
        #         return True
        #     for i in range(nums[_next]):
        #         if dfs(_next + i + 1):
        #             return True
        #     return False
        #
        # return dfs(0)

        # 动态规划
        # 超时
        if not nums:
            return True
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            for step in range(nums[i]):
                if dp[i + step + 1]:
                    dp[i] = True
                    break
        return dp[0]


print(Solution().canJump([3, 2, 1, 0, 4]))
