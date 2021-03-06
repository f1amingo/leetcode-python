from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] < nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                if nums[lo] == target:
                    return True
                lo += 1
        return True if nums[lo] == target else False


assert Solution().search([2, 5, 6, 0, 0, 1, 2], 0)
assert not Solution().search([2, 5, 6, 0, 0, 1, 2], 3)
