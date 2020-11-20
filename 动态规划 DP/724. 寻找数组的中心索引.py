from typing import List


class Solution:
    # 官方题解
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            # 右半边的和可以通过互补来求，不要再傻傻像和左边一样
            # 当有新信息时，往往也意味着更好的方法
            if leftSum == total - leftSum - num:
                return i
            leftSum += num
        return -1

    # 前缀和
    # def pivotIndex(self, nums: List[int]) -> int:
    #     if not nums:
    #         return -1
    #     n = len(nums)
    #     dp = [0] * (n + 1)
    #     for i in range(n):
    #         dp[i + 1] = dp[i] + nums[i]
    #     for i in range(n):
    #         if dp[i] == dp[-1] - dp[i + 1]:
    #             return i
    #     return -1


print(Solution().pivotIndex([-1, -1, -1, 0, 1, 1]))
print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([1, 2, 3]))
print(Solution().pivotIndex([1, 2, 1]))
