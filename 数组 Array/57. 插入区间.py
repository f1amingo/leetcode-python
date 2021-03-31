from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            # 左侧插入
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            # 右侧插入
            return intervals + [newInterval]
        ans = []
        lt, rt = newInterval
        flag = True
        for inter in intervals:
            if inter[1] < newInterval[0]:
                # 左侧不相交
                ans.append(inter)
            elif inter[0] > newInterval[1]:
                # 右侧不相交
                if flag:
                    # 第一次到右侧时，先加入新区间
                    ans.append([lt, rt])
                    flag = False
                ans.append(inter)
            else:
                lt = min(lt, inter[0])
                rt = max(rt, inter[1])
        if flag:
            ans.append([lt, rt])
        return ans


assert Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
