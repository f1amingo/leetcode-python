from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -0xffffff
        cur_min = cur_max = 1
        for num in nums:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(cur_max * num, num)
            cur_min = min(cur_min * num, num)
            res = max(res, cur_max)
        return res


nums = [2, 3, -2, -4]
print(Solution().maxProduct(nums))
print(Solution().maxProduct([-2, 0, -1]))
