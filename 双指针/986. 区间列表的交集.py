from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(A), len(B)
        i = j = 0
        cur = None
        while i < m or j < n:
            if i >= m:
                tmp = B[j]
                j += 1
            elif j >= n:
                tmp = A[i]
                i += 1
            else:
                if A[i] < B[j]:
                    tmp = A[i]
                    i += 1
                else:
                    tmp = B[j]
                    j += 1
            if cur:
                # 相交
                if tmp[0] <= cur[1]:
                    ans.append([tmp[0], min(tmp[1], cur[1])])
                # 更新
                if tmp[1] > cur[1]:
                    cur = tmp
            else:
                cur = tmp
        return ans


assert Solution().intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                                       [[1, 5], [8, 12], [15, 24], [25, 26]]) == [[1, 2], [5, 5], [8, 10], [15, 23],
                                                                                  [24, 24], [25, 25]]
