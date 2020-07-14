from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # # 标准二分法
        # if not nums:
        #     return 0
        # if target < nums[0]:
        #     return 0
        # n = len(nums)
        # if target > nums[-1]:
        #     return n
        # left, right = 0, n - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if target == nums[mid]:
        #         return mid
        #     elif target < nums[mid]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # # 这里退出循环后，left一定不等于right
        # return left

        # 排除法
        if target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums) - 1
        # 此方法产生的下标只可能在[0, n-1]内，只会是合法的
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


print(Solution().searchInsert([1, 3, 5, 6], 7))
