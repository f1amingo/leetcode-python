from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums and k > len(nums):
            return -1
        # 第K大，转换成第len(nums)-k小
        n_smallest = len(nums) - k

        # 模板
        def partition(low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1

        # [low, high]
        def quick_select(low, high):
            # 至少要有两个元素
            if low < high:
                p = partition(low, high)
                if p == n_smallest:
                    return nums[p]
                elif p < n_smallest:
                    return quick_select(p + 1, high)
                else:
                    return quick_select(low, p - 1)
            # 一个元素时
            return nums[low]

        return quick_select(0, len(nums) - 1)


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
