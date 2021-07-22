from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(A: List, i: int, j: int):
            pivot = A[i]
            m = i
            for k in range(i + 1, j):
                if A[k] < pivot:
                    m += 1
                    A[m], A[k] = A[k], A[m]
            A[m], A[i] = A[i], A[m]
            return m

        n = len(nums)
        k_small = n - k
        lo, hi = 0, n - 1
        while lo < hi:
            mid = partition(nums, lo, hi + 1)
            if mid < k_small:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
