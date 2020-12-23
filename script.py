from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_most = 0
        for i, num in enumerate(nums):
            if right_most < i:
                return False
            right_most = max(right_most, i + num)
        return True


assert Solution().canJump([2, 3, 1, 1, 4])
assert not Solution().canJump([3, 2, 1, 0, 4])
