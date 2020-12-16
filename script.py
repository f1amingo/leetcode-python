from typing import List


class Solution:
    # dp[i]使用前n数字能否凑出值i
    def canPartition(self, nums: List[int]) -> bool:
        C, mod = divmod(sum(nums), 2)
        if mod == 1:
            return False
        dp = [True] + [False] * C
        for num in nums:
            for c in range(C, num - 1, -1):
                dp[c] = dp[c] or dp[c - num]
        return dp[-1]


assert Solution().canPartition([1, 5, 11, 5])
assert not Solution().canPartition([1, 2, 3, 5])
