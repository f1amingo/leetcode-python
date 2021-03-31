from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == '+':
                stk[-2] = stk[-1] + stk[-2]
                stk.pop()
            elif token == '-':
                stk[-2] = stk[-2] - stk[-1]
                stk.pop()
            elif token == '*':
                stk[-2] = stk[-2] * stk[-1]
                stk.pop()
            elif token == '/':
                stk[-2] = int(stk[-2] / stk[-1])
                stk.pop()
            else:
                stk.append(int(token))
        return stk[0]


assert Solution().evalRPN(["4", "3", "-"]) == 1
assert Solution().evalRPN(
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
) == 22
assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
