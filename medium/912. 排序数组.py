from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, low, mid, high):
            N = high - low
            b = [0] * N
            p1, p2, bIdx = low, mid, 0
            while p1 < mid and p2 < high:
                if a[p1] <= a[p2]:
                    b[bIdx] = a[p1]
                    p1 += 1
                else:
                    b[bIdx] = a[p2]
                    p2 += 1
                bIdx += 1
            while p1 < mid:
                b[bIdx] = a[p1]
                p1 += 1
                bIdx += 1
            while p2 < high:
                b[bIdx] = a[p2]
                p2 += 1
                bIdx += 1
            for i in range(N):
                a[low + i] = b[i]

        def merge_sort(a, low, high):
            if low + 1 < high:
                mid = (low + high) // 2
                merge_sort(a, low, mid)
                merge_sort(a, mid, high)
                merge(a, low, mid, high)

        merge_sort(nums, 0, len(nums))

        return nums


a = [-2, 3, -5]
Solution().sortArray(a)
print(a)
