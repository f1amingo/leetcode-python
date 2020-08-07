from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums) // 2

        def partition(low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1

        def quick_select(low, high):
            if low < high:
                p = partition(low, high)
                if p == k:
                    return nums[p]
                elif p > k:
                    return quick_select(low, p - 1)
                else:
                    return quick_select(p + 1, high)
            else:
                return nums[low]

        return quick_select(0, len(nums) - 1)

