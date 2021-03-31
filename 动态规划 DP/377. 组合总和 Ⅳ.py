from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        # 为什么内外循环交换就不可以了
        # for num in nums:
        #     for i in range(num, target + 1):
        #         dp[i] = dp[i] + dp[i - num]
        return dp[-1]


assert Solution().combinationSum4([1, 2, 3], 4) == 7
