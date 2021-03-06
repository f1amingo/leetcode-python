from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # 只考虑后半部分
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi -= 1
        return nums[lo]

    # def findMin(self, nums: List[int]) -> int:
    #     # 和上一个问题类似
    #     if not nums:
    #         return 0
    #     if nums[0] < nums[-1]:
    #         return nums[0]
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         # 这里提前结束
    #         # 否则对于[3,1,3,3,3]
    #         # left++后，剩下的整体有序，继续下面的逻辑会把最小值排除
    #         # 但是如果针对右边界移动，就不会有这个问题
    #         if nums[left] < nums[right]:
    #             return nums[left]
    #         if nums[left] < nums[mid]:
    #             # [mid+1, right]中出现拐点
    #             left = mid + 1
    #         elif nums[left] > nums[mid]:
    #             # [left, mid]中出现拐点
    #             right = mid
    #         else:
    #             # [left]==[mid]的情况
    #             left += 1
    #     return nums[left]


print(Solution().findMin([10, 1, 10, 10, 10]))
print(Solution().findMin([10, 1, 10, 10, 10]))
