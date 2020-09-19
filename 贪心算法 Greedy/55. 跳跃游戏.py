from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        most_right = 0
        for i in range(len(nums)):
            if most_right < i:
                return False
            most_right = max(most_right, nums[i] + i)
        return True


assert Solution().canJump([2, 3, 1, 1, 4])
assert not Solution().canJump([3, 2, 1, 0, 4])
