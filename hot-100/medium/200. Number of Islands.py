from typing import List


class Solution:
    # My solution
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     row_count = len(grid)
    #     if not row_count:
    #         return 0
    #     col_count = len(grid[0])
    #
    #     def dfs(i, j):
    #         grid[i][j] = '0'
    #         if i - 1 >= 0 and grid[i - 1][j] == '1':
    #             dfs(i - 1, j)
    #         if j - 1 >= 0 and grid[i][j - 1] == '1':
    #             dfs(i, j - 1)
    #         if i + 1 < row_count and grid[i + 1][j] == '1':
    #             dfs(i + 1, j)
    #         if j + 1 < col_count and grid[i][j + 1] == '1':
    #             dfs(i, j + 1)
    #
    #     count = 0
    #     for i in range(row_count):
    #         for j in range(col_count):
    #             if grid[i][j] == '1':
    #                 count += 1
    #                 dfs(i, j)
    #     return count

    # 方向数组
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        stk = []
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    stk.append((i, j))
                    while stk:
                        x, y = stk.pop()
                        grid[x][y] = '0'
                        for direct in directions:
                            new_x, new_y = x + direct[0], y + direct[1]
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
                                stk.append((new_x, new_y))
                    res += 1
        return res


print(Solution().numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
