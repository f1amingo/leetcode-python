from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = []
        start, end = intervals[0]
        for lt, rt in intervals:
            # 不相交
            if end < lt:
                ans.append([start, end])
                start, end = lt, rt
            else:
                end = max(end, rt)
        ans.append([start, end])
        return ans


assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
