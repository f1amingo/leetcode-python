class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        stk = []
        for c in s:
            if c == '(':
                cnt += 1
                stk.append(c)
            elif c == ')':
                # 左括号多于右括号才可以入栈
                # 否则，前面没有左括号与其匹配
                if cnt > 0:
                    stk.append(c)
                    cnt -= 1
            else:
                stk.append(c)
        stk.reverse()
        # 遍历结束后，cnt不等于0，说明左括号多了cnt个
        for i in range(cnt):
            stk.remove('(')
        stk.reverse()
        return ''.join(stk)


print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
