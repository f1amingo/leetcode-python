from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        found = 0
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                _dst = i
                for j in range(i + 1, n):
                    if nums[i - 1] < nums[j] < nums[_dst]:
                        _dst = j
                nums[i - 1], nums[_dst] = nums[_dst], nums[i - 1]
                found = i
                break
        nums[found:] = sorted(nums[found:])


arr = [1,1,5]
Solution().nextPermutation(arr)
print(arr)
