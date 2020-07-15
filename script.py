from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        down, up = [0] * n, [0] * n
        down[0] = up[0] = 1
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            elif nums[i - 1] < nums[i]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[-1], down[-1])


print(Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]))
