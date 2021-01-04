from typing import List


# n x n矩阵
# 每行每列升序
# 第k小的元素
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 小于mid的元素数量
        def check(mid: int):
            i, j = n - 1, 0
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            # 如果count大于k，说明mid过大了，需要减小
            return count >= k

        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
