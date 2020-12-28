from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        size = m * n
        ans, idx = [0] * size, 0
        l, t, r, b = 0, 0, n - 1, m - 1
        while idx < size:
            for i in range(l, r + 1):
                ans[idx] = matrix[t][i]
                idx += 1
            if idx == size:
                break
            t += 1
            for i in range(t, b + 1):
                ans[idx] = matrix[i][r]
                idx += 1
            if idx == size:
                break
            r -= 1
            for i in range(r, l - 1, -1):
                ans[idx] = matrix[b][i]
                idx += 1
            if idx == size:
                break
            b -= 1
            for i in range(b, t - 1, -1):
                ans[idx] = matrix[i][l]
                idx += 1
            l += 1
        return ans


assert Solution().spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

assert Solution().spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
