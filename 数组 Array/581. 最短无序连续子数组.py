from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        min_val, max_val = float('inf'), float('-inf')
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                min_val = min(min_val, nums[i])
                max_val = max(max_val, nums[i - 1])
        lt, rt = 0, n - 1
        for lt in range(n):
            if nums[lt] > min_val:
                break
        for rt in range(n - 1, -1, -1):
            if nums[rt] < max_val:
                break
        return 0 if min_val == float('inf') else rt - lt + 1


assert Solution().findUnsortedSubarray([1, 2, 3, 4]) == 0
assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
