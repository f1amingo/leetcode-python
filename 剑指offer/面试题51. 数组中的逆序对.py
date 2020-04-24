from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge_sort(arr, tmp, low, high):
            if low < high:
                mid = (low + high) // 2
                a = merge_sort(arr, tmp, low, mid)
                b = merge_sort(arr, tmp, mid + 1, high)
                if arr[mid] <= arr[mid + 1]:
                    return a + b
                c = merge(arr, tmp, low, mid, high)
                return a + b + c
            return 0

        def merge(arr, tmp, low, mid, high):
            i, j, pos = low, mid + 1, low
            count = 0
            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    tmp[pos] = arr[i]
                    i += 1
                else:
                    tmp[pos] = arr[j]
                    j += 1
                    count += (mid - i + 1)
                pos += 1
            for k in range(i, mid + 1):
                tmp[pos] = arr[k]
                pos += 1
            for k in range(j, high + 1):
                tmp[pos] = arr[k]
                pos += 1
            arr[low:high + 1] = tmp[low:high + 1]
            return count

        n = len(nums)
        if n < 2:
            return 0
        tmp = [0] * n
        return merge_sort(nums, tmp, 0, n - 1)


print(Solution().reversePairs([7, 5, 6, 4]))
