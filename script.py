from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        cut_point = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                cut_point = i - 1
                break
        if cut_point != -1:
            max_i = cut_point + 1
            for i in range(cut_point + 1, n):
                if nums[max_i] > nums[i] > nums[cut_point]:
                    max_i = i
            nums[cut_point], nums[max_i] = nums[max_i], nums[cut_point]
        nums[cut_point + 1:] = sorted(nums[cut_point + 1:])


arr = [1,1,5]
Solution().nextPermutation(arr)
print(arr)
