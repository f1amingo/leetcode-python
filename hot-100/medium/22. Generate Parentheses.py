from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(cur, left, right):
            if right == 0:
                if cur:
                    ans.append(cur)
                return
            if left > 0:
                dfs(cur + '(', left - 1, right)
            if right > left:
                dfs(cur + ')', left, right - 1)

        dfs('', n, n)
        return ans


print(Solution().generateParenthesis(0))
