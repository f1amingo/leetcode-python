from typing import List


class Solution:
    # 迭代
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(A, lo, mid, hi, tmp):
            i, j, pos = lo, mid + 1, lo
            while i <= mid and j <= hi:
                # 等于，稳定性保证
                if A[i] <= A[j]:
                    tmp[pos] = A[i]
                    i += 1
                else:
                    tmp[pos] = A[j]
                    j += 1
                pos += 1
            for k in range(i, mid + 1):
                tmp[pos] = A[k]
                pos += 1
            for k in range(j, hi + 1):
                tmp[pos] = A[k]
                pos += 1
            A[lo:hi + 1] = tmp[lo:hi + 1]

        n = len(nums)
        tmp = [0] * n
        sz = 1  # 子数组大小
        while sz < n:
            lo = 0
            # 剩下的要能拆成两个sz
            while lo < n - sz:
                # merge相同
                merge(nums, lo, lo + sz - 1, min(lo + sz + sz - 1, n - 1), tmp)
                lo += sz + sz
            sz += sz
        return nums

    # 递归
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     def merge(A, lo, mid, hi, tmp):
    #         i, j, pos = lo, mid + 1, lo
    #         while i <= mid and j <= hi:
    #             # 等于，稳定性保证
    #             if A[i] <= A[j]:
    #                 tmp[pos] = A[i]
    #                 i += 1
    #             else:
    #                 tmp[pos] = A[j]
    #                 j += 1
    #             pos += 1
    #         for k in range(i, mid + 1):
    #             tmp[pos] = A[k]
    #             pos += 1
    #         for k in range(j, hi + 1):
    #             tmp[pos] = A[k]
    #             pos += 1
    #         A[lo:hi + 1] = tmp[lo:hi + 1]
    #
    #     # [lo, hi]
    #     def merge_sort(A, lo, hi, tmp):
    #         # 至少两个元素，如果等于只有一个元素，已经有序
    #         if lo < hi:
    #             # 奇怪的优先级
    #             # mid = lo + ((hi - lo) >> 1)
    #             mid = lo + (hi - lo) // 2
    #             merge_sort(A, lo, mid, tmp)
    #             merge_sort(A, mid + 1, hi, tmp)
    #             # 优化
    #             if A[mid] <= A[mid + 1]:
    #                 return
    #             merge(A, lo, mid, hi, tmp)
    #
    #     n = len(nums)
    #     merge_sort(nums, 0, n - 1, [0] * n)
    #     return nums


assert Solution().sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
assert Solution().sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
