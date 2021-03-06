from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(A: List, lo: int, mid: int, hi: int, tmp: List):
            i, j = lo, mid + 1
            pos = lo
            nonlocal ans
            while i <= mid and j <= hi:
                if A[i] <= A[j]:
                    tmp[pos] = A[i]
                    i += 1
                else:
                    tmp[pos] = A[j]
                    j += 1
                    ans += mid - i + 1
                pos += 1
            for k in range(i, mid + 1):
                tmp[pos] = A[k]
                pos += 1
            for k in range(j, hi + 1):
                tmp[pos] = A[k]
                pos += 1
            A[lo:hi + 1] = tmp[lo:hi + 1]

        def merge_sort(A: List, lo: int, hi: int, tmp: List):
            if lo < hi:
                mid = (lo + hi) // 2
                merge_sort(A, lo, mid, tmp)
                merge_sort(A, mid + 1, hi, tmp)
                if A[mid] <= A[mid + 1]:
                    return
                merge(A, lo, mid, hi, tmp)

        ans = 0
        merge_sort(nums, 0, len(nums) - 1, [0] * len(nums))
        return ans


assert Solution().reversePairs([7, 5, 6, 4]) == 5
