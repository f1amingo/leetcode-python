from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max = -0xffffff
        imax = imin = 1
        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            _max = max(_max, imax)
        return _max


print(Solution().maxProduct([-2,3,-4]))
