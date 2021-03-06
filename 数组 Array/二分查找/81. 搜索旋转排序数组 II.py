from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # 左半有序
            if nums[lo] < nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            # 右半有序
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid
            # 相等的情况
            else:
                if nums[lo] == target:
                    return True
                lo += 1
        return nums[lo] == target

    # def search(self, nums: List[int], target: int) -> bool:
    #     if not nums:
    #         return False
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         # [left, mid]严格递增
    #         if nums[left] < nums[mid]:
    #             if nums[left] <= target <= nums[mid]:
    #                 right = mid
    #             else:
    #                 left = mid + 1
    #         # 和上面的区间不要重叠
    #         # 否则只有两个数的时候，比如[2, 5]
    #         # left=2, mid=2, right=5
    #         # 会一直进入此判断分支，然后又left=mid，跳不出去
    #         # [mid+1, right]严格递增
    #         elif nums[mid + 1] < nums[right]:
    #             if nums[mid + 1] <= target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid
    #         else:
    #             # 特殊处理
    #             if nums[left] == target:
    #                 return True
    #             else:
    #                 # 移动一位
    #                 left += 1
    #     return nums[left] == target


print(Solution().search([2, 2, 2, 0, 2, 2], 0))
