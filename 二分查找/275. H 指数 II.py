from typing import List


# 已排序
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] > n - mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return n - lo


assert Solution().hIndex([100]) == 1
assert Solution().hIndex([0]) == 0
assert Solution().hIndex([0, 1, 3, 5, 6]) == 3
assert Solution().hIndex([1]) == 1
assert Solution().hIndex([]) == 0
