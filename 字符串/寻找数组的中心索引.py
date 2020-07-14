class Solution(object):
    # my solution
    # def pivotIndex(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     size = len(nums)
    #     if size == 0:
    #         return -1
    #     left = 0
    #     right = sum(nums) - nums[0]
    #     if left == right:
    #         return 0
    #     for i in range(1, size):
    #         left = left + nums[i - 1]
    #         right = right - nums[i]
    #         if left == right:
    #             return i
    #     return -1

    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for (i, num) in enumerate(nums):
            if left_sum * 2 + num == total_sum:
                return i
            left_sum += num
        return -1


print(Solution().pivotIndex([-1, -1, 0, 1, 1, 0]))
