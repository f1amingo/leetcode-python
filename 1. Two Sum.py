# 暴力
# 4284 ms	13 MB
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(0, len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         raise Exception('no solution found!')


# 字典二次遍历
# 88 ms	13.4 MB
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         this_map = {}
#         for i, num in enumerate(nums):
#             this_map[num] = i
#         for i, num in enumerate(nums):
#             complement = target - num
#             if this_map.get(complement) and this_map.get(complement) != i:
#                 return [i, this_map.get(complement)]
#         raise Exception('not found')

# 字典一次遍历
# 40 ms	13.1 MB
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        this_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if this_map.get(complement) is None:
                pass
            else:
                return [this_map.get(complement), i]
            this_map[num] = i


solution = Solution()
print(solution.twoSum([3, 3], 6))
