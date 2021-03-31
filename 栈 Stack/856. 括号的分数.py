class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stk = []
        for c in S:
            if c == '(':
                stk.append(c)
            else:
                token = stk.pop()
                total = 1
                if token != '(':
                    total = 0
                    while token != '(':
                        total += token
                        token = stk.pop()
                    total *= 2
                stk.append(total)
        return sum(stk)


assert Solution().scoreOfParentheses('()') == 1
assert Solution().scoreOfParentheses("(())") == 2
assert Solution().scoreOfParentheses("()()") == 2
assert Solution().scoreOfParentheses("(()(()))") == 6
