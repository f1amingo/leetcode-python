from typing import List


class Solution:
    # 一维dp
    # def rob(self, nums: List[int]) -> int:
    #     dp = [0] * (len(nums) + 2)
    #     for i in range(len(nums)):
    #         dpi = i + 2
    #         dp[dpi] = max(dp[dpi - 2] + nums[i], dp[dpi - 1])
    #     return dp[-1]

    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for num in nums:
            pre, cur = cur, max(pre + num, cur)
        return cur


print(Solution().rob([]))
print(Solution().rob([1]))
print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 7, 9, 3, 1]))
