from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0

        def merge(low, mid, high):
            i, j, k = low, mid, 0
            arr = [0] * (high - low)
            while i < mid and j < high:
                if nums[i] <= nums[j]:
                    arr[k] = nums[i]
                    i += 1
                else:
                    arr[k] = nums[j]
                    j += 1
                    nonlocal ans
                    ans += mid - i
                k += 1
            while i < mid:
                arr[k] = nums[i]
                k += 1
                i += 1
            while j < high:
                arr[k] = nums[j]
                k += 1
                j += 1
            nums[low:high] = arr

        def sort(low, high):
            if low < high - 1:
                mid = (low + high) // 2
                sort(low, mid)
                sort(mid, high)
                if nums[mid - 1] <= nums[mid]:
                    return
                merge(low, mid, high)

        sort(0, len(nums))
        return ans


print(Solution().reversePairs([7, 5, 6, 4]))
