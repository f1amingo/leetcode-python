from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N <= 3:
            return max(nums)

        def helper(left, right):
            n = right - left + 2
            dp = [0] * n
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i + left - 2], dp[i - 1])
            return dp[-1]

        return max(helper(0, N - 1), helper(1, N))


print(Solution().rob([1]))
print(Solution().rob([2, 3, 2]))
print(Solution().rob([1, 2, 3, 1]))
