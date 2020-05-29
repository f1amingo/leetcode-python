class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        this_max = 1
        for i in range(1, n):
            cur_max = 0
            for j in range(i):
                if nums[i] > nums[j] and dp[j] > cur_max:
                    cur_max = dp[j]
            dp[i] = cur_max + 1
            if dp[i] > this_max:
                this_max = dp[i]
        return this_max


# print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
print(Solution().lengthOfLIS([0]))
