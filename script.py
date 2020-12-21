from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = max_val = min_val = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_val, min_val = min_val, max_val
            max_val = max(max_val * num, num)
            min_val = min(min_val * num, num)
            ans = max(ans, max_val)
        return ans


assert Solution().maxProduct([-2]) == -2
assert Solution().maxProduct([2, 3, -2, 4]) == 6
assert Solution().maxProduct([-2, 0, -1]) == 0
