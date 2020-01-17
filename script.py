from typing import List


class Solution:
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

