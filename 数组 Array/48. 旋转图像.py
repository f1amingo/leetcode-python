from typing import List


# 大小n x n
# 旋转90度 in place
class Solution:
    # 原地旋转
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        n = len(matrix)
        i = 0
        while i < n // 2:
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp
            i += 1


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Solution().rotate(matrix)
for l in matrix:
    print(l)
