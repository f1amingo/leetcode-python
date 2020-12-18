from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(low, high):
            pivot = nums[low]
            m = low
            for i in range(low + 1, high):
                if nums[i] < pivot:
                    m += 1
                    nums[m], nums[i] = nums[i], nums[m]
            nums[low], nums[m] = nums[m], nums[low]
            return m

        def quick_find(low, high):
            if low < high:
                m = partition(low, high)
                if m == k_smallest:
                    return nums[m]
                elif m < k_smallest:
                    return quick_find(m + 1, high)
                else:
                    return quick_find(low, m)

        k_smallest = len(nums) - k
        return quick_find(0, len(nums))
