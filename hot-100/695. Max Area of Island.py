from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_count = len(grid)
        col_count = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = []
        max_area = 0
        for i in range(row_count):
            for j in range(col_count):
                if grid[i][j] == 0:
                    continue
                queue.append((i, j))
                grid[i][j] = 0
                area = 1
                while queue:
                    top_ele = queue.pop()
                    for direct in directions:
                        new_i, new_j = top_ele[0] + direct[0], top_ele[1] + direct[1]
                        if -1 < new_i < row_count and -1 < new_j < col_count:
                            if grid[new_i][new_j] == 1:
                                queue.append((new_i, new_j))
                                grid[new_i][new_j] = 0
                                area += 1
                if area > max_area:
                    max_area = area
        return max_area


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(Solution().maxAreaOfIsland(grid))
