class Solution:
    # official solution
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                  (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        res = []
        # 这是一个O(1)的算法
        for value, symbol in digits:
            if num == 0:
                break
            # python居然还有这样一个函数
            count, num = divmod(num, value)
            # 字符串乘法 'C'*3='CCC'
            res.append(symbol * count)
        return ''.join(res)
    # my solution
    # def intToRoman(self, num: int) -> str:
    #     values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    #     symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    #     res = []
    #     # 会遍历太多次
    #     while num:
    #         for i in range(len(values)):
    #             if num >= values[i]:
    #                 break
    #         res.append(symbols[i])
    #         num -= values[i]
    #     return ''.join(res)


print(Solution().intToRoman(3))
print(Solution().intToRoman(4))
print(Solution().intToRoman(9))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
