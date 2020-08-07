from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        tmp = 0
        for num in nums:
            if tmp > 0:
                tmp += num
            else:
                tmp = num
            res = max(res, tmp)
        return res


print(Solution().maxSubArray([-2, -1]))
