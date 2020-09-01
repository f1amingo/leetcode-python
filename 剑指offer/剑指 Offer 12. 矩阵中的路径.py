from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        m, n, len_s = len(board), len(board[0]), len(word)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, wanted, visited):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or wanted >= len_s:
                return False
            visited.add((i, j))
            if board[i][j] == word[wanted]:
                if wanted == len_s - 1:
                    return True
                else:
                    for direction in directions:
                        if dfs(i + direction[0], j + direction[1], wanted + 1, visited):
                            return True
            visited.remove((i, j))
            return False

        visited = set()
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, visited):
                    return True
        return False


bor = [["a", "b"], ["c", "d"]]
print(Solution().exist(bor, "bacd"))
