from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while 1 <= nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        return N + 1


assert Solution().firstMissingPositive([1, 2, 3]) == 4
