from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 运载能力为capacity时，需要几天可以运完
        def countDays(capacity: int) -> int:
            count = 1
            tmp = capacity
            for w in weights:
                if tmp >= w:
                    tmp -= w
                else:
                    count += 1
                    tmp = capacity - w
            return count

        # 下界是最重的物品，不然就运不走这个物品
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) >> 1
            if D < countDays(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo


assert Solution().shipWithinDays([1, 2, 3, 1, 1], 4) == 3
assert Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
assert Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6
