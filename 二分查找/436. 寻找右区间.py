from typing import List


class Solution:

    # 排序+二分
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        index_map = {}
        for i in range(n):
            index_map[tuple(intervals[i])] = i
        intervals.sort()
        ans = [-1] * n
        for i in range(n - 1):
            lo, hi = i + 1, n - 1
            while lo < hi:
                mid = (lo + hi) >> 1
                if intervals[mid][0] >= intervals[i][1]:
                    hi = mid
                else:
                    lo = mid + 1
            if intervals[lo][0] >= intervals[i][1]:
                ans[index_map[tuple(intervals[i])]] = index_map[tuple(intervals[lo])]
        return ans

    # 哈希表+排序+扫描
    # def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    #     n = len(intervals)
    #     index_map = {}
    #     for i in range(n):
    #         index_map[tuple(intervals[i])] = i
    #     intervals.sort()
    #     ans = [-1] * n
    #     for i in range(n - 1):
    #         for j in range(i + 1, n):
    #             if intervals[j][0] >= intervals[i][1]:
    #                 ans[index_map[tuple(intervals[i])]] = index_map[tuple(intervals[j])]
    #                 break
    #     return ans

    # 暴力超时
    # def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    #     n = len(intervals)
    #     ans = [-1] * n
    #     for i in range(n):
    #         lt, rt = float('inf'), float('inf')
    #         idx = -1
    #         for j in range(n):
    #             if i == j:
    #                 continue
    #             if intervals[i][1] <= intervals[j][0] < lt:
    #                 lt, rt = intervals[j]
    #                 idx = j
    #         ans[i] = idx
    #     return ans


assert Solution().findRightInterval([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]) == [3, 3, 3, 4, 5, -1]
assert Solution().findRightInterval([[3, 4], [2, 3], [1, 2]]) == [-1, 0, 1]
assert Solution().findRightInterval([[1, 2]]) == [-1]
assert Solution().findRightInterval([[1, 4], [2, 3], [3, 4]]) == [-1, 2, -1]
