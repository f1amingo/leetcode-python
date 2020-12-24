from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(lt: int, rt: int, cur_list: List):
            if lt == 0 and rt == 0:
                ans.append(''.join(cur_list))
                return
            if lt > 0:
                # 可以添加左括号
                cur_list.append('(')
                dfs(lt - 1, rt, cur_list)
                cur_list.pop()
            if rt > lt:
                # 剩下的右括号多余左括号
                cur_list.append(')')
                dfs(lt, rt - 1, cur_list)
                cur_list.pop()

        ans = []
        dfs(n, n, [])
        return ans


print(Solution().generateParenthesis(3))
