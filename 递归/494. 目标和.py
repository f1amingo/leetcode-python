from typing import List


class Solution:
    # 01背包
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        C, mod = divmod(sum(nums) - S, 2)
        # C应该为正数或0
        # 整数数组，除不尽，直接返回零
        if C < 0 or mod != 0:
            return 0

        dp = [1] + [0] * C
        for num in nums:
            for c in range(C, num - 1, -1):
                dp[c] += dp[c - num]
        return dp[-1]

    # 超时
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     n = len(nums)
    #     ans = 0
    #
    #     def dfs(cur_sum: int, i: int):
    #         if i == n:
    #             if cur_sum == S:
    #                 nonlocal ans
    #                 ans += 1
    #             return
    #         dfs(cur_sum + nums[i], i + 1)
    #         dfs(cur_sum - nums[i], i + 1)
    #
    #     dfs(0, 0)
    #     return ans


assert Solution().findTargetSumWays([1, 2, 7, 9, 981], 1000000000) == 0
assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
