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

        # 如何判断取左中位数，还是右中位数
        # 考虑仅有两个元素时，mid=(lo+hi)//2，mid此时等于lo
        # 若此时进入第一个分支，执行lo=mid，此次循环没有缩小边界，导致死循环
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

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if not nums:
    #         return [-1, -1]
    #
    #     def lower_bound(A: List[int], t: int):
    #         left, right = 0, len(A) - 1
    #         while left < right:
    #             mid = (left + right) // 2
    #             # 为什么能找到下界
    #             # 等于的时候，left不会动，right不断逼近left
    #             if t > A[mid]:
    #                 left = mid + 1
    #             else:
    #                 right = mid
    #         return left if A[left] == target else -1
    #
    #     def higher_bound(A: List[int], t: int):
    #         left, right = 0, len(A) - 1
    #         while left < right:
    #             # 这里取右中位数
    #             mid = (left + right) // 2 + 1
    #             if t < A[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid
    #         return left
    #
    #     lower = lower_bound(nums, target)
    #     if lower == -1:
    #         return [-1, -1]
    #     return [lower, higher_bound(nums, target)]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
