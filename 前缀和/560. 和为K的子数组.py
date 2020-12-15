from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        pre_sum = 0
        total = 0
        for num in nums:
            pre_sum += num
            # k可能等于0
            total += lookup.get(pre_sum - k, 0)
            lookup[pre_sum] = lookup.get(pre_sum, 0) + 1
        return total


assert Solution().subarraySum([1], 0) == 0
assert Solution().subarraySum([1, 1, 1], 2) == 2
