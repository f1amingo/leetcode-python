class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        number = 0
        times = 0
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
            if lookup[num] > times:
                times = lookup[num]
                number = num
        return number


print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
