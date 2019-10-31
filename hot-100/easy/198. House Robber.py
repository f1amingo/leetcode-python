class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的解法
        # if not nums:
        #     return 0
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # dp = [0] * n
        # for i in range(n):
        #     if i == 0 or i == 1:
        #         dp[i] = nums[i]
        #     else:
        #         if i - 2 > 0:
        #             dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
        #         else:
        #             dp[i] = nums[i] + dp[i - 2]
        # return max(dp[-1], dp[-2])

        # 参考后修改
        # if not nums:
        #     return 0
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # if n > 1:
        #     dp[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        # return dp[-1]

        # 前面补零 避免if
        # nums = [0, 0] + nums
        # for i in range(2, len(nums)):
        #     nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        # return nums[-1]

        # O(1)的空间
        last = now = 0
        for i in nums:
            last, now = now, max(now, last + i)
        return now


print(Solution().rob([1, 2, 3, 1]))
