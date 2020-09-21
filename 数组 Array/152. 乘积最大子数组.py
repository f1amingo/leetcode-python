from typing import List


class Solution:
    # 当num<0时，最大值、最小值会发生转换
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        cur_min = nums[0]
        cur_max = nums[0]
        _max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i], cur_max * nums[i])
            cur_min = min(nums[i], cur_min * nums[i])
            _max = max(_max, cur_max)
        return _max


print(Solution().maxProduct([-2, 3, -4]))
