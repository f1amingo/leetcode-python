from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        C = total // 2
        dp = [0] * (C + 1)
        for num in nums:
            for v in range(C, num - 1, -1):
                dp[v] = max(dp[v], dp[v - num] + num)
        return dp[-1] == C


print(Solution().canPartition([23, 13, 11, 7, 6, 5, 5]))
