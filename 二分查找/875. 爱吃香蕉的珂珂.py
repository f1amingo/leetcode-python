from typing import List
import math


# 一堆至少一小时
# 二分法避免死循环：左中位数就一定要保证更新左边界时，lo = mid + 1
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 以speed的速度吃香蕉需要花费的时间
        def timeCost(speed: int) -> int:
            return sum([math.ceil(p / speed) for p in piles])

        # 最少每小时1个，最多每小时max(piles)个
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if timeCost(mid) <= H:
                # 吃太快，速度慢一点
                hi = mid
            else:
                # 吃太慢，速度快一点
                lo = mid + 1
        return lo


assert Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4
assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
