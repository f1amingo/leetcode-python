from typing import List


class Solution:

    # 在新数组上操作
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # res = matrix.copy() 浅拷贝要不得！！！
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n - i - 1] = matrix[i][j]
        # matrix = res 你TM这样写上过专业课吗！？
        matrix[:] = res

    # 翻转代替旋转
    # 画个图找下规律：1.沿主对角线翻转；2.沿竖向对称轴翻转
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     n = len(matrix)
    #     for i in range(n - 1):
    #         for j in range(i + 1, n):
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #     for i in range(n):
    #         for j in range(n // 2):
    #             matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    # 原地旋转
    # 四连swap，坐标推导心中要有图，注意对称关系、不变量
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     n = len(matrix)
    #     for i in range(n // 2):
    #         for j in range(i, n - i - 1):
    #             tmp = matrix[i][j]
    #             matrix[i][j] = matrix[n - j - 1][i]
    #             matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
    #             matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
    #             matrix[j][n - i - 1] = tmp


m = [
    [1, 2],
    [3, 4]
]
# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
Solution().rotate(m)
print(m)
