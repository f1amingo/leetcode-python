class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = []
        level = 0
        for c in S:
            if c == '(':
                level += 1
            if level > 1:
                ans.append(c)
            if c == ')':
                level -= 1
        return ''.join(ans)

    # 对左右括号计数
    # def removeOuterParentheses(self, S: str) -> str:
    #     ans = []
    #     stk = []
    #     lt_count = rt_count = 0
    #     for c in S:
    #         if c == '(':
    #             stk.append(c)
    #             lt_count += 1
    #         else:
    #             stk.append(c)
    #             rt_count += 1
    #             if rt_count == lt_count:
    #                 ans.append(''.join(stk[1:-1]))
    #                 stk.clear()
    #     return ''.join(ans)


assert Solution().removeOuterParentheses("(()())(())") == "()()()"
assert Solution().removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
assert Solution().removeOuterParentheses("()()") == ""
