from typing import List


class Solution:
    # 自底向上
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if not obstacleGrid or not obstacleGrid[0]:
            return []
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = obstacleGrid[0][0] == 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if (i - 1 >= 0 and dp[i - 1][j]) or (j - 1 >= 0 and dp[i][j - 1]):
                        dp[i][j] = True

        res = []
        if dp[m - 1][n - 1]:
            # 重构路径
            x, y = m - 1, n - 1
            while x != 0 or y != 0:
                res.append([x, y])
                if x > 0 and dp[x - 1][y]:
                    x -= 1
                else:
                    y -= 1
            res.append([0, 0])
            res.reverse()
        return res

    # 记忆化递归
    # 自顶向下
    # def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
    #     if not obstacleGrid or not obstacleGrid[0]:
    #         return []
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     memo = [[None] * n for _ in range(m)]
    #
    #     # 从(i,j)是否可达(0,0)
    #     def f(i: int, j: int) -> bool:
    #         # 当前位置[i, j]没有障碍物
    #         if obstacleGrid[i][j] == 0:
    #             # 已经到达[0, 0]
    #             if i == 0 and j == 0:
    #                 memo[i][j] = True
    #                 return True
    #             else:
    #                 # 从上方到达[i, j]的路径
    #                 # 前提是上方的格子有意义
    #                 if i - 1 >= 0:
    #                     if memo[i - 1][j] is None:
    #                         memo[i][j] = f(i - 1, j)
    #                     if memo[i][j]:
    #                         return True
    #                 # 从左方到达[i, j]的路径
    #                 # 前提是左方的格子有意义
    #                 if j - 1 >= 0:
    #                     if memo[i][j - 1] is None:
    #                         memo[i][j] = f(i, j - 1)
    #                     if memo[i][j]:
    #                         return True
    #         # [i, j]到[0, 0]不可达
    #         return False
    #
    #     res = [[m - 1, n - 1]]
    #     x, y = m - 1, n - 1
    #     if f(m - 1, n - 1):
    #         # 回溯重构路径
    #         while x != 0 or y != 0:
    #             if x > 0 and memo[x - 1][y]:
    #                 x -= 1
    #             else:
    #                 y -= 1
    #             res.append([x, y])
    #         res.reverse()
    #         return res
    #     else:
    #         return []

    # 递归
    # def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
    #     if not obstacleGrid or not obstacleGrid[0]:
    #         return []
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #
    #     # 返回从[0, 0]到[i, j]的路径，包括[i, j]
    #     # 若不存在，返回[]
    #     def f(i: int, j: int) -> List[List[int]]:
    #         # 当前位置[i, j]没有障碍物
    #         if obstacleGrid[i][j] == 0:
    #             # 已经到达[0, 0]
    #             if i == 0 and j == 0:
    #                 return [[0, 0]]
    #             else:
    #                 top_path = right_path = None
    #                 # 从上方到达[i, j]的路径
    #                 # 前提是上方的格子有意义
    #                 if i - 1 >= 0:
    #                     top_path = f(i - 1, j)
    #                 # 如果从上方可达，提前返回
    #                 if top_path:
    #                     return top_path + [[i, j]]
    #                 # 从左方到达[i, j]的路径
    #                 # 前提是左方的格子有意义
    #                 if j - 1 >= 0:
    #                     right_path = f(i, j - 1)
    #                 if right_path:
    #                     return right_path + [[i, j]]
    #         # [i, j]到[0, 0]不可达
    #         return []
    #
    #     return f(m - 1, n - 1)


print(Solution().pathWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))

print(Solution().pathWithObstacles([
    [1]
]))
