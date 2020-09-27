from typing import List


class Solution:
    # 使用第一行、第一列来进行标记
    # 不使用额外空间
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix and not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        # 标记初始状态，因为后面会直接修改在第一行、第一列
        is_row_contains_zero = is_col_contains_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                is_col_contains_zero = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                is_row_contains_zero = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if is_col_contains_zero:
            for i in range(m):
                matrix[i][0] = 0
        if is_row_contains_zero:
            for j in range(n):
                matrix[0][j] = 0


mat = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
Solution().setZeroes(mat)
print(mat)
