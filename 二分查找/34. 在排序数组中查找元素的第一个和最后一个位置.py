from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def lower_bound(A: List[int], t: int):
            left, right = 0, len(A) - 1
            while left < right:
                mid = (left + right) // 2
                # 为什么能找到下界
                # 等于的时候，left不会动，right不断逼近left
                if t > A[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left if A[left] == target else -1

        def higher_bound(A: List[int], t: int):
            left, right = 0, len(A) - 1
            while left < right:
                # 这里取右中位数
                mid = (left + right) // 2 + 1
                if t < A[mid]:
                    right = mid - 1
                else:
                    left = mid
            return left

        lower = lower_bound(nums, target)
        if lower == -1:
            return [-1, -1]
        return [lower, higher_bound(nums, target)]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
