from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n < 2:
            return
        pivot = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        if pivot != -1:
            for i in range(n - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


nums = [3, 2, 1]
Solution().nextPermutation(nums)
print(nums)
