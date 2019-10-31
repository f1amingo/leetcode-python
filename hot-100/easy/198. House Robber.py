class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的解法
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        for i in range(n):
            if i == 0 or i == 1:
                dp[i] = nums[i]
            else:
                if i - 2 > 0:
                    dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
                else:
                    dp[i] = nums[i] + dp[i - 2]
        return max(dp[-1], dp[-2])


print(Solution().rob([6, 8, 1]))
