from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(A: List, i: int, j: int):
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


A = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(A, 3)
assert A == [5, 6, 7, 1, 2, 3, 4]

A = [1]
Solution().rotate(A, 2)
assert A == [1]