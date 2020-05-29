class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total_sum = sum(nums)
        if total_sum < S or (total_sum + S) & 1:
            return 0
        sum_p = (total_sum + S) // 2
        dp = [1] + [0] * sum_p
        for num in nums:
            for i in range(sum_p, num - 1, - 1):
                dp[i] = dp[i] + dp[i - num]
        return dp[-1]


print(Solution().findTargetSumWays([7, 9, 3, 8, 0, 2, 4, 8, 3, 9], 0))
