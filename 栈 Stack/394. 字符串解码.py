class Solution:
    def decodeString(self, s: str) -> str:
        stk, res, times = [], '', 0
        for c in s:
            if c == '[':
                stk.append((res, times))
                res, times = '', 0
            elif c == ']':
                # 不要覆盖原times
                last_res, last_times = stk.pop()
                res = last_res + last_times * res
            elif '0' <= c <= '9':
                times = times * 10 + int(c)
            else:
                res += c
        return res

    # [也入栈
    # def decodeString(self, s: str) -> str:
    #     stk = []
    #     for c in s:
    #         if c == ']':
    #             single = ''
    #             while stk[-1] != '[':
    #                 single = stk.pop() + single
    #             stk.pop()
    #             times = ''
    #             while stk and stk[-1].isdigit():
    #                 times = stk.pop() + times
    #             times = int(times)
    #             stk.append(single * times)
    #         else:
    #             stk.append(c)
    #     return ''.join(stk)


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
