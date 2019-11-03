class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # using counter
        count = [0] * len(nums)
        for i in nums:
            count[i - 1] += 1
        res = []
        for i in range(len(nums)):
            if count[i] == 0:
                res.append(i + 1)
        return res


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
