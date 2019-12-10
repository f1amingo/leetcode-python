from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_count = len(grid)
        if not row_count:
            return 0
        col_count = len(grid[0])

        def dfs(i, j):
            grid[i][j] = '0'
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                dfs(i - 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                dfs(i, j - 1)
            if i + 1 < row_count and grid[i + 1][j] == '1':
                dfs(i + 1, j)
            if j + 1 < col_count and grid[i][j + 1] == '1':
                dfs(i, j + 1)

        count = 0
        for i in range(row_count):
            for j in range(col_count):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count


print(Solution().numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
