from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ans = max(ans, (right - left) * height[left])
                left += 1
            else:
                ans = max(ans, (right - left) * height[right])
                right -= 1
        return ans


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
