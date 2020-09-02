from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            while i != num:
                if num == nums[num]:
                    return num
                nums[i], nums[num] = nums[num], nums[i]
        return -1


print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
