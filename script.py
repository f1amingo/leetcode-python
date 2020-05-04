from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPos, n = 0, len(nums)
        for i in range(n):
            if maxPos < i:
                return False
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= n - 1:
                return True
        return True


assert Solution().canJump([2, 3, 1, 1, 4])
assert not Solution().canJump([3, 2, 1, 0, 4])
assert Solution().canJump([])
