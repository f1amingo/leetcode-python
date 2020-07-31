from typing import List


class Solution:

    # 跳跃优化
    def findMagicIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == nums[i]:
                return i
            elif i < nums[i]:
                i = nums[i]
            else:
                i += 1
        return -1
    # 朴素遍历
    # def findMagicIndex(self, nums: List[int]) -> int:
    #     if not nums:
    #         return -1
    #     for i in range(len(nums)):
    #         if i == nums[i]:
    #             return i
    #     return -1
