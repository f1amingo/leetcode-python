class Solution(object):
    # 二维数组
    def canPartition0(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        this_sum = sum(nums)
        if this_sum % 2 == 1:
            return False
        target = this_sum // 2
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        for i in range(target + 1):
            dp[0][i] = False if nums[0] != i else True
        for i in range(1, n):
            for j in range(1, target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[-1][-1]

    def canPartition(self, nums):
        this_sum = sum(nums)
        if this_sum % 2 != 0:
            return False
        target = this_sum // 2
        n = len(nums)
        dp = [False for _ in range(target + 1)]
        for i in range(target + 1):
            dp[i] = True if nums[0] == i else False
        for i in range(1, n):
            for j in range(target, 0, -1):
                if j > nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]


print(Solution().canPartition([1, 5, 11, 5]))
