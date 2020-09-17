from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        parent = [[(i, j) for j in range(n)] for i in range(m)]

        def find(pos: (int, int)) -> (int, int):
            x, y = pos
            if parent[x][y] != pos:
                parent[x][y] = find(parent[x][y])
            return parent[x][y]

        def union(p: (int, int), q: (int, int)):
            pRoot, qRoot = find(p), find(q)
            parent[pRoot[0]][pRoot[1]] = qRoot

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    right = (i, min(j + 1, n - 1))
                    bottom = (min(i + 1, m - 1), j)
                    this_parent = find((i, j))
                    if grid[right[0]][right[1]] == '1':
                        rpx, rpy = find(right)
                        parent[rpx][rpy] = this_parent
                    if grid[bottom[0]][bottom[1]] == '1':
                        bpx, bpy = find(bottom)
                        parent[bpx][bpy] = this_parent
        res_map = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res_map[find((i, j))] = 1

        return len(res_map)


assert Solution().numIslands([
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]) == 1

assert Solution().numIslands([
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]) == 3

assert Solution().numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]) == 1

assert Solution().numIslands([["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]]) == 1
