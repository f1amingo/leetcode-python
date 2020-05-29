from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(low, high):
            p = nums[low]
            m = low
            for i in range(low + 1, high):
                if nums[i] < p:
                    m += 1
                    nums[m], nums[i] = nums[i], nums[m]
            nums[low], nums[m] = nums[m], nums[low]
            return m

        k_smallest = len(nums) - k

        def quick_find(low, high):
            if low < high:
                m = partition(low, high)
                if m == k_smallest:
                    return nums[m]
                elif m < k_smallest:
                    return quick_find(m + 1, high)
                else:
                    return quick_find(low, m)
            return nums[low]

        return quick_find(0, len(nums))


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
