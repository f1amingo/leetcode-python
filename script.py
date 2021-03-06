from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] > nums[mid]:  # 前半无序
                hi = mid
            elif nums[mid] > nums[hi]:  # 前半有序
                lo = mid + 1
            else:  # 前后都有序
                return min(nums[lo], nums[mid + 1])
        return nums[lo]


assert Solution().findMin([3, 4, 5, 1, 2]) == 1
assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert Solution().findMin([1]) == 1
