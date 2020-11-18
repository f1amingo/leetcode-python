from typing import List


class Solution:
    # 动态规划（前缀和）超时
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * (n + 1)
        res = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if dp[j] - dp[i - 1] == k:
                    res += 1
        return res


assert Solution().subarraySum([-1, -1, 1], 0) == 1
assert Solution().subarraySum([1], 0) == 0
assert Solution().subarraySum([1, 1, 1], 2) == 2
assert Solution().subarraySum([1], 1) == 1
