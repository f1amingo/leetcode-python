class Solution:
    # 大值的左边存在小值时，减去小值
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        values = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        res = 0
        preNum = values[s[0]]
        for i in range(1, len(s)):
            num = values[s[i]]
            if preNum < num:
                res -= preNum
            else:
                res += preNum
            preNum = num
        return res + preNum

    # my solution
    # 逐位相加
    # def romanToInt(self, s: str) -> int:
    #     digits = {
    #         'M': 1000,
    #         'CM': 900,
    #         'D': 500,
    #         'CD': 400,
    #         'C': 100,
    #         'XC': 90,
    #         'L': 50,
    #         'XL': 40,
    #         'X': 10,
    #         'IX': 9,
    #         'V': 5,
    #         'IV': 4,
    #         'I': 1,
    #     }
    #
    #     ptr = 0
    #     n = len(s)
    #     res = 0
    #     while ptr < n - 1:
    #         digit = s[ptr:ptr + 2]
    #         if digit in digits:
    #             res += digits[digit]
    #             ptr += 2
    #         else:
    #             res += digits[s[ptr]]
    #             ptr += 1
    #     # 最后一位别忘记处理
    #     if ptr < n:
    #         res += digits[s[-1]]
    #     return res


print(Solution().romanToInt('III'))
print(Solution().romanToInt('IV'))
print(Solution().romanToInt('IX'))
print(Solution().romanToInt('LVIII'))
print(Solution().romanToInt('MCMXCIV'))
