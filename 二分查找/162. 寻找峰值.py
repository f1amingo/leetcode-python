from typing import List


# 因为nums[-1]和nums[n]无穷小，所以沿着上升段爬升，最终一定会下降
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


print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
