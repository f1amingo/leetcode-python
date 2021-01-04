from typing import List


# 某个点上旋转，可能仍然有序
# 原数组：[1,2,3,4,5]
# 在2上旋转：[3,4,5,1,2]
# 在5上旋转：[1,2,3,4,5] (不变)
# 找出最小元素
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            # 整体有序lo即为最小
            if nums[lo] <= nums[hi]:
                return nums[lo]
            mid = (lo + hi) // 2
            # 整体无序
            if nums[lo] <= nums[mid]:
                # 前半有序，后半无序，最小值在后半
                lo = mid + 1
            else:
                # 前半无序，后半有序，最小值可能是mid，也可能在前半
                hi = mid
        return nums[lo]


assert Solution().findMin([3, 4, 5, 1, 2]) == 1
assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert Solution().findMin([1]) == 1
