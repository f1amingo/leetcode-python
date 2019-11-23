from typing import List
import copy


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # my solution
        n = len(intervals)
        if n <= 1:
            return intervals
        ans = []
        sorted_list = sorted(intervals, key=lambda x: x[0])
        p1 = copy.copy(sorted_list[0])
        for i in range(1, n):
            p2 = sorted_list[i]
            if p1[0] <= p2[0] and p1[1] >= p2[1]:
                pass
            elif p1[1] >= p2[0]:
                p1 = [p1[0], p2[1]]
            else:
                ans.append(p1)
                p1 = copy.copy(p2)
        ans.append(p1)
        return ans


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [2, 3]]))
print(Solution().merge([[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]))
