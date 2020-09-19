from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        # 按照区间末尾排序
        points.sort(key=lambda x: x[1])
        # 当前箭能覆盖的最远位置
        end = points[0][1]
        res = 1
        for i in range(1, len(points)):
            # 覆盖不到，就需要一只新箭
            if points[i][0] > end:
                end = points[i][1]
                res += 1
        return res


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
