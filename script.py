from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] >= target:
                    hi = mid
            return lo if nums[lo] == target else -1

        def findRight():
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                # 右中位数
                mid = (lo + hi) // 2 + 1
                if nums[mid] <= target:
                    lo = mid
                elif nums[mid] > target:
                    hi = mid - 1
            return lo if nums[lo] == target else -1

        if not nums:
            return [-1, -1]
        lt = findLeft()
        if lt == -1:
            return [-1, -1]
        return [lt, findRight()]


assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
