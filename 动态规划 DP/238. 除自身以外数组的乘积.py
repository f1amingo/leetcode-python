from typing import List


class Solution:
    # 前缀和后缀乘积
    # 思想类似动态规划，缓存子问题结果
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1] * (n + 1), [1] * (n + 1)
        res = [0] * n
        for i in range(1, n + 1):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 1, -1, -1):
            right[i] = right[i + 1] * nums[i]
        for i in range(n):
            res[i] = left[i] * right[i + 1]
        return res

    # 暴力，超时
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #
    #     def dfs(i: int) -> int:
    #         p = 1
    #         for j in range(n):
    #             if j != i:
    #                 p *= nums[j]
    #         return p
    #
    #     return [dfs(i) for i in range(n)]


print(Solution().productExceptSelf([1, 2, 3, 4]))
