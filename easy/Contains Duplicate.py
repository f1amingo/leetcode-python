class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup = {}
        for num in nums:
            if num in lookup:
                return True
            else:
                lookup[num] = 0
        return False


print(Solution().containsDuplicate([1, 2, 3, 4]))
