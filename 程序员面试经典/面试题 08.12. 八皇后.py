from typing import List


# 不要觉得回溯很厉害，本质就是暴力
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 这个递归函数的工作：为第i行放置一个皇后
        def placeRowN(i: int):
            if i == n:
                # 所有行都填完了，加入结果
                _item = [['.'] * n for _ in range(n)]
                for k in range(n):
                    _item[k][rows[k]] = 'Q'
                    _item[k] = ''.join(_item[k])
                res.append(_item)
                return
            # 对于每一行中的每一列逐个尝试
            for j in range(n):
                # 这就是所谓的剪枝，进入递归需满足条件
                # 这题的其余解法都是剪枝方法上的区别，当然你也可以用位运算，或者就是简单while遍历一下
                if j not in columns and i + j not in diagonals1 and i - j not in diagonals2:
                    # 更新一下新状态
                    rows[i] = j
                    columns.add(j)
                    diagonals1.add(i + j)
                    diagonals2.add(i - j)
                    placeRowN(i + 1)
                    # 复原状态，也被称为回溯
                    rows[i] = -1
                    columns.remove(j)
                    diagonals1.remove(i + j)
                    diagonals2.remove(i - j)

        res = []
        rows = [-1] * n  # 初始值多少并无影响，但最好给一个没有意义的值，虽然-1在python中还是有意义的。。
        diagonals1 = set()
        diagonals2 = set()
        columns = set()

        placeRowN(0)
        return res


print(Solution().solveNQueens(4))
