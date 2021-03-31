from typing import List


class Solution:
    # 递归，accepted，很慢
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0

        # 以(i,j)为左上角，k为边长的正方形是否合法
        def dfs(i, j, k) -> bool:
            for x in range(i, i + k):
                if grid[x][j] == 0 or grid[x][j + k - 1] == 0:
                    return False
            for y in range(j, j + k):
                if grid[i][y] == 0 or grid[i + k - 1][y] == 0:
                    return False
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(1, res)
                    for k in range(2, min(m - i, n - j) + 1):
                        if dfs(i, j, k):
                            res = max(res, k)
        return res * res


assert Solution().largest1BorderedSquare([[0, 0, 0, 1]]) == 1
assert Solution().largest1BorderedSquare([[1]]) == 1
assert Solution().largest1BorderedSquare([[1, 1, 0, 0]]) == 1
assert Solution().largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 9
