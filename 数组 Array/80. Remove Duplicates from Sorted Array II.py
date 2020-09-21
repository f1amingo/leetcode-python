class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i可插入位置 num当前位置
        i = 0
        for num in nums:
            if i < 2:
                i += 1
            elif num != nums[i - 2]:
                nums[i] = num
                i += 1
        return i


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
