from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 思想：相邻两点决定的最小线段，如果上升则峰值在右边；否则峰值在左边
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 这里比较的是mid和mid+1
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


print(Solution().findPeakElement([1,2,1,3,5,6,4]))
