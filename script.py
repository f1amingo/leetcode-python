from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        maxPos, step, end = 0, 0, 0
        for i in range(len(nums)):
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= len(nums) - 1:
                return step + 1
            if i == end:
                end = maxPos
                step += 1
        return step


print(Solution().jump([2, 3, 1, 1, 4]))
print(Solution().jump([1]))
