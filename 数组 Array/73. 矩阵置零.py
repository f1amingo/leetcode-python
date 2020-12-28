from typing import List


class Solution:
    # O(1) 空间复杂度
    # 标记第一行、第一列，但要注意其本身含有0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_row = flag_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                flag_row = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag_row:
            for j in range(n):
                matrix[0][j] = 0
        if flag_col:
            for i in range(m):
                matrix[i][0] = 0

    # O(m + n) 空间复杂度
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     if not matrix or not matrix[0]:
    #         return
    #     m, n = len(matrix), len(matrix[0])
    #     row, col = [False] * m, [False] * n
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 row[i] = col[j] = True
    #     for i in range(m):
    #         for j in range(n):
    #             if row[i] or col[j]:
    #                 matrix[i][j] = 0


matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
Solution().setZeroes(matrix)
print(matrix)
