from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        dp = [1] * n
        maxL = 1
        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i] + 1)
            maxL = max(maxL, dp[j])
        return maxL


assert Solution().lengthOfLIS([]) == 0
assert Solution().lengthOfLIS([1]) == 1
assert Solution().lengthOfLIS([1, 2]) == 2
assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
