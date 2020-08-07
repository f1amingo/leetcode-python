from typing import List


class Solution:

    # 方法四：快速选择第len(nums)//2个元素
    # 超时
    # def majorityElement(self, nums: List[int]) -> int:
    #     k = len(nums) // 2
    #
    #     def partition(low, high):
    #         pivot = nums[high]
    #         i = low - 1
    #         for j in range(low, high):
    #             if nums[j] <= pivot:
    #                 i += 1
    #                 nums[i], nums[j] = nums[j], nums[i]
    #         nums[i + 1], nums[high] = nums[high], nums[i + 1]
    #         return i + 1
    #
    #     def quick_select(low, high):
    #         if low < high:
    #             p = partition(low, high)
    #             if p == k:
    #                 return nums[p]
    #             elif p > k:
    #                 return quick_select(low, p - 1)
    #             else:
    #                 return quick_select(p + 1, high)
    #         else:
    #             return nums[low]
    #
    #     return quick_select(0, len(nums) - 1)

    # 方法三：Moore投票法
    def majorityElement(self, nums: List[int]) -> int:
        cur, votes = -1, 0
        for num in nums:
            if votes == 0:
                cur = num
            votes += 1 if cur == num else -1
        return cur

    # 方法二：排序
    # def majorityElement(self, nums: List[int]) -> int:
    #     # 当有两个元素时，取到右边的元素
    #     # 当有一个元素时，取到自身
    #     # 所以不用加一，也不用减一
    #     return sorted(nums)[len(nums) // 2]

    # 方法一：遍历使用hash统计
    # def majorityElement(self, nums: List[int]) -> int:
    #     n, found = len(nums), {}
    #     for num in nums:
    #         found[num] = found.get(num, 0) + 1
    #         if found[num] > n // 2:
    #             return num
    #     return -1


print(Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
