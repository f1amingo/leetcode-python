from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = maxP = minP = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                minP, maxP = maxP, minP
            minP = min(nums[i], nums[i] * minP)
            maxP = max(nums[i], nums[i] * maxP)
            res = max(res, maxP)
        return res


print(Solution().maxProduct([2, 3, -2, 4]))
print(Solution().maxProduct([-2,0,-1]))
