from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        for item in intervals:
            if item[0] <= right:
                right = max(right, item[1])
            elif item[0] <= left and item[1] <= right:
                pass
            else:
                res.append([left, right])
                left = item[0]
                right = item[1]
        res.append([left, right])
        return res


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [4, 5]]))
print(Solution().merge([]))
