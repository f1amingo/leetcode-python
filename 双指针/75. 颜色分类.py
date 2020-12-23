from typing import List


class Solution:
    # 双指针
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1

    # 单指针
    # def sortColors(self, nums: List[int]) -> None:
    #     ptr = 0
    #     for i in range(len(nums)):
    #         if nums[i] == 0:
    #             nums[i], nums[ptr] = nums[ptr], nums[i]
    #             ptr += 1
    #     ptr = len(nums) - 1
    #     for i in range(len(nums) - 1, -1, -1):
    #         if nums[i] == 2:
    #             nums[i], nums[ptr] = nums[ptr], nums[i]
    #             ptr -= 1


Solution().sortColors([2, 0, 2, 1, 1, 0])

nums = [1, 2, 0]
Solution().sortColors(nums)
assert nums == [0, 1, 2]
