from typing import List


# 时间复杂度 O(m+n)
# 好好体会这题和二分的区别
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        # i, j = m, 0 第一次写错了，低级错误
        i, j = m - 1, 0
        while i > -1 and j < n:
            if target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                return True
        return False
