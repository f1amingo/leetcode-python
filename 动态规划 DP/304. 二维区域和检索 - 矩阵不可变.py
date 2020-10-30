from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.empty = True
            return
        self.empty = False
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    # j==0时，j-1=-1，此时这排的最后一个元素为0，所以结果是对的
                    # 只有一个元素也是正确的
                    dp[0][j] = dp[0][j - 1] + matrix[0][j]
                elif j == 0:
                    dp[i][0] = dp[i - 1][0] + matrix[i][0]
                else:
                    # 画图一看就懂了
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + matrix[i][j]
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.empty:
            return 0
        # 边界处理
        # 多给一行一列的空间会幸福很多
        a = 0 if row1 - 1 < 0 else self.dp[row1 - 1][col2]
        b = 0 if col1 - 1 < 0 else self.dp[row2][col1 - 1]
        c = 0 if row1 - 1 < 0 or col1 - 1 < 0 else self.dp[row1 - 1][col1 - 1]
        return self.dp[row2][col2] - a - b + c

    # Your NumMatrix object will be instantiated and called as such:


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(0, 0, 0, 0))
print(obj.sumRegion(0, 0, 1, 1))
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
assert obj.sumRegion(2, 1, 4, 3) == 8
assert obj.sumRegion(1, 1, 2, 2) == 11
assert obj.sumRegion(1, 2, 2, 4) == 12
