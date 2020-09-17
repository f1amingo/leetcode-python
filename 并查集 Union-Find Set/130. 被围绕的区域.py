from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        def find(p: int) -> int:
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]

        def union(p: int, q: int):
            parent[find(q)] = find(p)

        m, n = len(board), len(board[0])
        dummy = m * n
        parent = [i for i in range(dummy + 1)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    this_index = i * n + j
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        union(this_index, dummy)
                    else:
                        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            x, y = i + x, j + y
                            # 这里只union 'O'
                            if board[x][y] == 'O':
                                union(this_index, x * n + y)
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    if find(i * n + j) != find(dummy):
                        board[i][j] = 'X'


Solution().solve(
    [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"],
     ["X", "X", "O", "X", "O"]])
