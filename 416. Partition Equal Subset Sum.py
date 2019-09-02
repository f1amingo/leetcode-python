class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        dp = [[False for _ in range(target + 1)] for _ in range(size)]
        for i in range(1, size):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
