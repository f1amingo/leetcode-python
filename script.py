from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        C, mod = divmod(sum(nums), 2)
        if mod != 0:
            return False
        dp = [False] * (C + 1)
        dp[0] = True
        for num in nums:
            for i in range(C, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[-1]


assert Solution().canPartition([1, 5, 11, 5])
assert not Solution().canPartition( [1, 2, 3, 5])
