from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        rows = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    idx = ord(board[i][j]) - ord('1')
                    grid_i = (i // 3) * 3 + j // 3
                    if grids[grid_i][idx] or cols[j][idx] or rows[i][idx]:
                        return False
                    grids[grid_i][idx] = cols[j][idx] = rows[i][idx] = True
        return True


assert Solution().isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])
