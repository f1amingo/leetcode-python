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
        # if not nums:
        #     return True
        # n = len(nums)
        # dp = [False] * n
        # dp[-1] = True
        # for i in range(n - 2, -1, -1):
        #     for step in range(nums[i]):
        #         if dp[i + step + 1]:
        #             dp[i] = True
        #             break
        # return dp[0]

        # 优化状态转移方程
        # 超时
        # if not nums:
        #     return True
        # n = len(nums)
        # dp = [False] * n
        # dp[-1] = True
        # for i in range(n - 2, -1, -1):
        #     end_include = min(i + nums[i], n - 1)
        #     for j in range(i + 1, end_include + 1):
        #         if dp[j]:
        #             dp[i] = True
        #             break
        # return dp[0]

        # 考虑最远能跳到的位置
        n = len(nums)
        max_jump = 0
        for i in range(n):
            if i > max_jump:
                return False
            if max_jump >= n:
                return True
            max_jump = max(max_jump, i + nums[i])
        return True


print(Solution().canJump([3, 2, 1, 0, 4]))
