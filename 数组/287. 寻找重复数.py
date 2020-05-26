from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i + 1 != nums[i]:
                idx = nums[i] - 1
                if nums[idx] == nums[i]:
                    return nums[i]
                else:
                    nums[i], nums[idx] = nums[idx], nums[i]
        return -1


print(Solution().findDuplicate([3,1,3,4,2]))
