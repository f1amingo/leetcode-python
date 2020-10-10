from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # lt_count, rt_count: 还可以放置的左右括号数目
        def dfs(cur: str, lt_count: int, rt_count: int):
            if lt_count == 0 and rt_count == 0:
                res.append(cur)
                return
            if lt_count > 0:
                dfs(cur + '(', lt_count - 1, rt_count)
            # 之前放置了更多的'('，才可以放')'
            # 表象就是剩下的'('应该比')'更少
            if lt_count < rt_count:
                dfs(cur + ')', lt_count, rt_count - 1)

        res = []
        dfs('', n, n)
        return res


print(Solution().generateParenthesis(3))
