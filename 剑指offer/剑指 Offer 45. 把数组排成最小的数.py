import functools
from typing import List


class Solution:
    # 内置排序
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)

    # 快速排序
    # def minNumber(self, nums: List[int]) -> str:
    #     def partition(A, low, high):
    #         pivot = A[high]
    #         i = low - 1
    #         for j in range(low, high):
    #             if A[j] + pivot <= pivot + A[j]:
    #                 # if A[j] <= pivot:
    #                 i += 1
    #                 A[i], A[j] = A[j], A[i]
    #         A[i + 1], A[high] = A[high], A[i + 1]
    #         return i + 1
    #
    #     def quick_sort(A, low, high):
    #         if low < high:
    #             m = partition(A, low, high)
    #             quick_sort(A, low, m - 1)
    #             quick_sort(A, m + 1, high)
    #
    #     strs = [str(x) for x in nums]
    #     quick_sort(strs, 0, len(strs) - 1)
    #     return ''.join(strs)


print(Solution().minNumber([9, 3, 30, 34, 5]))
