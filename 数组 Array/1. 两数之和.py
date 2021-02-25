from typing import List


# 整数数组，正负数
# 两个数的和为目标值
# 返回两个数的下标
# 可重复，每个数只能用一次
class Solution:
    # 哈希表：时间O(n)，空间O(n)
    # 暴力慢是因为查找target-num太慢，
    # 因此可以使用hash map保存出现过的数字、下标
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            tmp = target - num
            if tmp in lookup:
                return [lookup[tmp], i]
            lookup[num] = i

    # 暴力：O(n^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]


assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
assert Solution().twoSum([3, 3], 6) == [0, 1]
