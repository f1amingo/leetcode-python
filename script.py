from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sorted_list = sorted(intervals)
        res = []
        left = right = None
        for inter in sorted_list:
            if left is None and right is None:
                left = inter[0]
                right = inter[1]
            else:
                if right < inter[0]:
                    res.append([left, right])
                    left = inter[0]
                    right = inter[1]
                elif right < inter[1]:
                    right = inter[1]
        res.append([left, right])
        return res


print(Solution().merge([[1, 4], [2, 3]]))
