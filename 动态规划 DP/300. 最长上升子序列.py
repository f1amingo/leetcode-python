from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # python优美是第一位的
        return max(dp)


assert Solution().lengthOfLIS([]) == 0
assert Solution().lengthOfLIS([1]) == 1
assert Solution().lengthOfLIS([1, 2]) == 2
assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
