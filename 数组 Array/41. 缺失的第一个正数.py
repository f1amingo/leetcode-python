from typing import List


# 未排序，整数，找未出现的最小正整数
# 时间O(n)，空间O(1)
class Solution:
    # 原地hash，把nums[i]放到nums[nums[i]-1]
    # 正整数 -> 数组下标
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 下标不越界
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1  # 存下来
                nums[i], nums[j] = nums[j], nums[i]
        for i, num in enumerate(nums):
            if i != num - 1:
                return i + 1
        # 走到这里说明，数组形如[1,2,3,...,N]，第一个未出现的正数为 N+1
        return size + 1  # 没写出来

    # 先加入hash表，然后从1开始枚举
    # 时间O(N)，空间O(N)
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     lookup = set(nums)
    #     ans = 1
    #     while ans in lookup:
    #         ans += 1
    #     return ans

    # 排序后从左往右找，O(NlogN)
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 1
    #     nums.sort()
    #     ans = 1
    #     for num in nums:
    #         if ans > 0:
    #             if ans == num:
    #                 ans += 1
    #     return ans


assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2
assert Solution().firstMissingPositive([1, 2, 0]) == 3
assert Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1
