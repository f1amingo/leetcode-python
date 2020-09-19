from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 2:
            return 0
        intervals.sort()
        prev = intervals[0]
        res = 0
        for i in range(1, n):
            this = intervals[i]
            if this[0] >= prev[1]:
                # 不相交
                prev = this
            else:  # this[0] < prev[1]
                if prev[1] < this[1]:
                    # prev与this部分相交
                    # 移除this，因为this的右边界可能还与其他区域相交
                    res += 1
                else:
                    # prev完全包住this
                    # 保留this
                    prev = this
                    res += 1
        return res


assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
