class Solution:
    def strToInt(self, s: str) -> int:
        if not s:
            return 0
        ptr, n = 0, len(s)
        while ptr < n and s[ptr] == ' ':
            ptr += 1
        sign = '+'
        if ptr < n:
            if s[ptr] == '+' or s[ptr] == '-':
                sign = s[ptr]
                ptr += 1
        num = 0
        # 这里判断数字的方式
        while ptr < n and '0' <= s[ptr] <= '9':
            num = num * 10 + int(s[ptr])
            ptr += 1
        if sign == '-':
            num = -num
        int_max = 2 ** 31 - 1
        if num > int_max:
            return int_max
        int_min = -2 ** 31
        if num < int_min:
            return int_min
        return num


print(Solution().strToInt("-91283472332"))
