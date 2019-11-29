from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left_most = 0
        for i in range(len(nums)):
            if left_most < i:
                return False
            left_most = max(left_most, i + nums[i])
        return True


print(Solution().canJump([3, 2, 1, 0, 4]))
