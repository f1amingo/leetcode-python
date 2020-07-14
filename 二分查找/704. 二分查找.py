from typing import List


class Solution:
    # 排除法
    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if target > nums[mid]:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return left if nums[left] == target else -1

    # 正常写法
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
