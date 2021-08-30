from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]


    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     dp = [1] + [0] * target
    #     for num in nums:
    #         for i in range(1, target + 1):
    #             if i >= num:
    #                 dp[i] += dp[i - num]
    #     return dp[-1]


assert Solution().combinationSum4([1, 2, 3], 4) == 7
assert Solution().combinationSum4([9], 3) == 0
