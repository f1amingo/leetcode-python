class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ']':
                single = ''
                while stk[-1] != '[':
                    single = stk.pop() + single
                stk.pop()
                times = ''
                while stk and stk[-1].isdigit():
                    times = stk.pop() + times
                times = int(times)
                stk.append(single * times)
            else:
                stk.append(c)
        return ''.join(stk)


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
