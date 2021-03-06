from typing import List


# 某个点上旋转，可能仍然有序
# 原数组：[1,2,3,4,5]
# 在2上旋转：[3,4,5,1,2]
# 在5上旋转：[1,2,3,4,5] (不变)
# 找出最小元素
class Solution:
    def findMin(self, nums: List[int]) -> int:
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

    # def findMin(self, nums: List[int]) -> int:
    #     if not nums:
    #         return
    #     lo, hi = 0, len(nums) - 1
    #     while lo < hi:
    #         # 整体有序lo即为最小
    #         if nums[lo] <= nums[hi]:
    #             return nums[lo]
    #         mid = (lo + hi) // 2
    #         # 整体无序
    #         if nums[lo] <= nums[mid]:
    #             # 前半有序，后半无序，最小值在后半
    #             lo = mid + 1
    #         else:
    #             # 前半无序，后半有序，最小值可能是mid，也可能在前半
    #             hi = mid
    #     return nums[lo]

    # def findMin(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     # 此时说明整体有序
    #     if nums[0] <= nums[-1]:
    #         return nums[0]
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         # [mid, right]有序，mid是后半部分最小的元素，是一个候选值
    #         if nums[mid] < nums[right]:
    #             right = mid
    #         # [mid, right]无序，那么最小值一定在无序部分
    #         # 因为数组的无序是因为，最小值处有一个转折导致的
    #         else:
    #             left = mid + 1
    #     return nums[left]


print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
