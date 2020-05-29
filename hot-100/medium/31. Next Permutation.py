from typing import List


class Solution:
    # 自己的解法 排序
    # def nextPermutation(self, nums: List[int]) -> None:
    #     if not nums:
    #         return
    #     n = len(nums)
    #     found = 0
    #     for i in range(n - 1, 0, -1):
    #         if nums[i - 1] < nums[i]:
    #             _dst = i
    #             for j in range(i + 1, n):
    #                 if nums[i - 1] < nums[j] < nums[_dst]:
    #                     _dst = j
    #             nums[i - 1], nums[_dst] = nums[_dst], nums[i - 1]
    #             found = i
    #             break
    #     nums[found:] = sorted(nums[found:])

    # 官方题解
    # 1.自右找前一个小于后一个的位置 pivot
    # 2.自右找大于pivot第一个位置 交换
    # 3.[pivot+1:]逆序（之前为降序）
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n < 2:
            return
        pivot = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        if pivot != -1:
            for i in range(n - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


arr = [1, 1, 5]
Solution().nextPermutation(arr)
print(arr)
