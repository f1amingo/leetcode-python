from typing import List


class Solution:
    # my solution
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        total, pos = m * n, 0
        ans = [0] * total
        top, right, bottom, left = 0, n - 1, m - 1, 0
        while pos < total:
            for i in range(left, right + 1):
                ans[pos] = matrix[top][i]
                pos += 1
            top += 1
            if pos >= total: break
            for i in range(top, bottom + 1):
                ans[pos] = matrix[i][right]
                pos += 1
            right -= 1
            if pos >= total: break
            for i in range(right, left - 1, -1):
                ans[pos] = matrix[bottom][i]
                pos += 1
            bottom -= 1
            if pos >= total: break
            for i in range(bottom, top - 1, -1):
                ans[pos] = matrix[i][left]
                pos += 1
            left += 1
        return ans


print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
