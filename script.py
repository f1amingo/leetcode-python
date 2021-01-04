from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


assert Solution().findPeakElement([1, 2, 3, 1]) == 2
assert Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
