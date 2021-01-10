from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        right = float('-inf')
        for inter in intervals:
            if inter[1] <= right:
                ans += 1
            else:
                right = inter[1]
        return len(intervals) - ans


assert Solution().removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]) == 1
assert Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]) == 2
