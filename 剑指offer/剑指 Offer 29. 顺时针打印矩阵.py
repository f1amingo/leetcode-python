from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []

        def print_circle(start: int):
            end_i = m - start
            end_j = n - start
            for j in range(start, end_j):
                res.append(matrix[start][j])
            delta_i = end_i - start
            delta_j = end_j - start
            # 高度至少为2，才有第2步
            if delta_i >= 2:
                for i in range(start + 1, end_i):
                    res.append(matrix[i][end_j - 1])
            # 高度至少为2，宽度至少为2
            if delta_i >= 2 and delta_j >= 2:
                for j in range(end_j - 2, start - 1, -1):
                    res.append(matrix[end_i - 1][j])
            # 高度至少为3，宽度至少为2
            if delta_i >= 3 and delta_j >= 2:
                for i in range(end_i - 2, start, -1):
                    res.append(matrix[i][start])

        start = 0
        while 2 * start < m and 2 * start < n:
            print_circle(start)
            start += 1
        return res


print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
