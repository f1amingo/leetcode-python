from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        row_count = len(board)
        col_count = len(board[0])
        queue = []
        for i in range(row_count):
            for j in range(col_count):
                if board[i][j] == word[0]:
                    queue.append([(i, j)])
        while queue:
            cur_list = queue.pop()
            if len(cur_list) == len(word):
                return True
            last_pos = cur_list[-1]
            candidates = [(last_pos[0] - 1, last_pos[1]),
                          (last_pos[0], last_pos[1] - 1),
                          (last_pos[0] + 1, last_pos[1]),
                          (last_pos[0], last_pos[1] + 1), ]
            for candi in candidates:
                if 0 <= candi[0] < row_count and 0 <= candi[1] < col_count:
                    if candi not in cur_list and board[candi[0]][candi[1]] == word[len(cur_list)]:
                        queue.append(cur_list + [candi])
        return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "SEE"
print(Solution().exist(board, word))
