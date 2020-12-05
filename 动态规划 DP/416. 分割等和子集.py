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

    # def canPartition(self, nums: List[int]) -> bool:
    # 朴素01背包
    # total = sum(nums)
    # if total % 2 == 1:
    #     return False
    # C = total // 2
    # dp = [0] * (C + 1)
    # for num in nums:
    #     for j in range(C, num - 1, -1):
    #         dp[j] = max(dp[j], dp[j - num] + num)
    # return dp[-1] == C

    # bool运算更快
    # dp[i]：前k个数字是否可以凑出C
    # total = sum(nums)
    # if total % 2 == 1:
    #     return False
    # C = total // 2
    # dp = [False] * (C + 1)
    # dp[0] = True
    # for num in nums:
    #     for j in range(C, num - 1, -1):
    #         dp[j] = dp[j] or dp[j - num]
    # return dp[-1]


# print(Solution().canPartition([1, 5, 11, 5]))
print(Solution().canPartition([1, 2, 5]))
