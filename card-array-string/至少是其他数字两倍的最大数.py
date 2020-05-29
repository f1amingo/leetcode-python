class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        max_i = -1
        second_max_num = 0
        for (i, num) in enumerate(nums):
            if num > max_num:
                second_max_num = max_num
                max_num = num
                max_i = i
            if second_max_num < num < max_num:
                second_max_num = num
        if max_num >= 2 * second_max_num:
            return max_i
        else:
            return -1


print(Solution().dominantIndex([0, 0, 3, 2]))
