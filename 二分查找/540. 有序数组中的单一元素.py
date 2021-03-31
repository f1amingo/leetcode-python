from typing import List


class Solution:
    # 画图，就单一元素出现在左半和右半分别讨论
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        if lo == hi:  # 单个元素
            return nums[lo]
        while lo < hi:
            mid = (lo + hi) // 2
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    lo = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    hi = mid - 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid + 1]:
                    lo = mid + 2
                elif nums[mid] == nums[mid - 1]:
                    hi = mid - 2
                else:
                    return nums[mid]
        return nums[lo]


assert Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
assert Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
