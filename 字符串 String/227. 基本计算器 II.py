class Solution:

    # 很强的lambda
    # 很聪明的边界处理
    def calculate(self, s: str) -> int:
        stk = []
        op_dict = {
            '+': lambda e: stk.append(e),
            '-': lambda e: stk.append(-e),
            '*': lambda e: stk.append(stk.pop() * e),
            '/': lambda e: stk.append(int(stk.pop() / e)),
        }
        num, op = 0, '+'
        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c != ' ':
                op_dict[op](num)
                num, op = 0, c
        return sum(stk)

    # def calculate(self, s: str) -> int:
    #     stk = []
    #     num, sign = 0, '+'
    #     len_s = len(s)
    #     for i in range(len_s):
    #         if s[i].isdigit():
    #             num = num * 10 + (ord(s[i]) - ord('0'))
    #         if s[i] in '+-*/' or i == len_s - 1:
    #             if sign == '+':
    #                 stk.append(num)
    #             elif sign == '-':
    #                 stk.append(-num)
    #             elif sign == '*':
    #                 stk.append(stk.pop() * num)
    #             else:
    #                 stk.append(int(stk.pop() / num))
    #             num, sign = 0, s[i]
    #     return sum(stk)

    # # 好好看看自己丑陋的代码！！！
    # def calculate(self, s: str) -> int:
    #     stk = []
    #     num, sign = 0, '+'
    #     for ch in s:
    #         if ch == '+' or ch == '-' or ch == '*' or ch == '/':
    #             if sign == '+':
    #                 stk.append(num)
    #             elif sign == '-':
    #                 stk.append(-num)
    #             elif sign == '*':
    #                 stk.append(stk.pop() * num)
    #             else:
    #                 op1 = stk.pop()
    #                 if op1 < 0:
    #                     stk.append(-(-op1 // num))
    #                 else:
    #                     stk.append(op1 // num)
    #             num, sign = 0, ch
    #         elif ch == ' ':
    #             pass
    #         else:
    #             num = num * 10 + (ord(ch) - ord('0'))
    #     if sign == '+':
    #         stk.append(num)
    #     elif sign == '-':
    #         stk.append(-num)
    #     elif sign == '*':
    #         stk.append(stk.pop() * num)
    #     else:
    #         op1 = stk.pop()
    #         if op1 < 0:
    #             stk.append(-(-op1 // num))
    #         else:
    #             stk.append(op1 // num)
    #     return sum(stk)


assert Solution().calculate("14-3/2") == 13
assert Solution().calculate("2*3+4") == 10
assert Solution().calculate("1-1+1") == 1
assert Solution().calculate("3+2*2") == 7
assert Solution().calculate(" 3/2 ") == 1
assert Solution().calculate(" 3+5 / 2 ") == 5
