from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        # [0..i]子序列中最长上升序列的长度
        up, down = [0] * n, [0] * n
        up[0] = down[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                down[i] = down[i - 1]
                up[i] = up[i - 1]
        return max(down[-1], up[-1])


print(Solution().wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
print(Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]))
