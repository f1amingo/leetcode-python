from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        max_i = 0
        for i in range(n):
            if max_i < i:
                return False
            max_i = max(max_i, i + nums[i])
            if max_i >= n - 1:
                return True
        return True


print(Solution().canJump([3, 2, 1, 0, 4]))
