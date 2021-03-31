from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, i: int) -> bool:
            if i == len(word):
                return True
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y]:
                return False
            if board[x][y] == word[i]:
                visited[x][y] = True
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if dfs(x + dx, y + dy, i + 1):
                        visited[x][y] = False
                        return True
                visited[x][y] = False
            return False

        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


assert Solution().exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], 'ABCCED')
assert Solution().exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], 'SEE')
assert not Solution().exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], 'ABCB')
