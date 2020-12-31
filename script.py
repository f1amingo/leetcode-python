from typing import List


# 非负整数数组
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        C, mod = divmod(sum(nums) - S, 2)
        if C < 0 or mod == 1:
            return 0
        dp = [1] + [0] * C
        for num in nums:
            for i in range(C, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
        return dp[-1]


assert Solution().findTargetSumWays([1, 2, 7, 9, 981], 1000000000) == 1
assert Solution().findTargetSumWays([1000], -1000) == 1
assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
