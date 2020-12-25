from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        lo, hi = 0, n - 1
        ans = 0
        while lo < hi:
            if height[lo] < height[hi]:
                ans = max(ans, (hi - lo) * height[lo])
                lo += 1
            else:
                ans = max(ans, (hi - lo) * height[hi])
                hi -= 1
        return ans


assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution().maxArea([1, 1]) == 1
assert Solution().maxArea([4, 3, 2, 1, 4]) == 16
assert Solution().maxArea([1, 2, 1]) == 2
