from typing import List


class Solution:
    # 01背包
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        C, mod = divmod(sum(nums) - S, 2)
        # C必须是一个正数，除不尽凑不出
        if C < 0 or mod != 0:
            return 0
        dp = [0] * (C + 1)
        dp[0] = 1
        for num in nums:
            # 不能重复选，倒序
            for i in range(C, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]


assert Solution().findTargetSumWays([1, 2, 7, 9, 981], 1000000000) == 0
assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
