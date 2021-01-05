from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        mn = m + n
        i, j = 0, 0
        pre, cur = 0, 0
        while i + j <= mn // 2:
            if i >= m:
                pre, cur = cur, nums2[j]
                j += 1
                continue
            if j >= n:
                pre, cur = cur, nums1[i]
                i += 1
                continue
            if nums1[i] <= nums2[j]:
                pre, cur = cur, nums1[i]
                i += 1
            else:
                pre, cur = cur, nums2[j]
                j += 1
        if mn % 2 == 1:
            return cur
        else:
            return (pre + cur) / 2


assert Solution().findMedianSortedArrays([], [1]) == 1
assert Solution().findMedianSortedArrays([1], []) == 1
assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
