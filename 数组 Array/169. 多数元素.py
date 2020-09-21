from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


assert Solution().majorityElement([3, 2, 3]) == 3
assert Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
