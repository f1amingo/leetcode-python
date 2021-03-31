class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ')':
                token, tmp = stk.pop(), ''
                while token != '(':
                    tmp = tmp + token
                    token = stk.pop()
                for t in tmp:
                    stk.append(t)
            else:
                stk.append(c)
        return ''.join(stk)


assert Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode"
assert Solution().reverseParentheses("(u(love)i)") == "iloveu"
assert Solution().reverseParentheses("(abcd)") == "dcba"
