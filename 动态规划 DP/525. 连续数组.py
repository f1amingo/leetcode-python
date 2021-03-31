from typing import List


# 数据量50k，时间复杂度O(n)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        maxLen = 0
        found = {0: -1}  # 初始化
        count = 0  # 相对值
        for i in range(n):
            count += (1 if nums[i] == 1 else -1)
            if count in found:
                maxLen = max(maxLen, i - found.get(count))
            else:
                found[count] = i
        return maxLen

    # 前缀和，超时
    # def findMaxLength(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n < 2:
    #         return 0
    #     res = 0
    #     # dp[i] [0:i]区间内zero_count - one_count的值
    #     dp = [0] * (n + 1)
    #     for i in range(1, n + 1):
    #         if nums[i - 1] == 0:
    #             dp[i] = dp[i - 1] + 1
    #         else:
    #             dp[i] = dp[i - 1] - 1
    #     for i in range(1, n + 1):
    #         if n - i + 1 <= res:
    #             break
    #         for j in range(i + 1, n + 1):
    #             if dp[j] - dp[i - 1] == 0:
    #                 res = max(res, j - i + 1)
    #     return res


assert Solution().findMaxLength([0, 1]) == 2
assert Solution().findMaxLength([0, 0, 0, 1, 1, 1, 0]) == 6
assert Solution().findMaxLength([0, 1, 0]) == 2
