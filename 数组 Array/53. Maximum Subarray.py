class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = None
        ans = None
        for i in nums:
            if sum is None:
                sum = i
                ans = i
                continue
            if sum > 0:
                sum = sum + i
            else:
                sum = i
            if ans < sum:
                ans = sum
        return ans


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([-1, 0, -2]))
