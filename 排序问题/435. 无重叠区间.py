from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        # 之前区间能覆盖的最远位置
        end = float('-inf')
        for inter in intervals:
            # 起点落在覆盖范围内
            if inter[0] < end:
                ans += 1
                end = min(end, inter[1])
            else:
                end = inter[1]
        return ans


assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
