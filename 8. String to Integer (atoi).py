# 48 ms	11.7 MB
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_strip = str.strip()
        start_index = 0
        is_minus = False
        if len(str_strip) < 1:
            return 0
        if str_strip[0].isnumeric():
            pass
        elif str_strip[0] == '+':
            start_index = 1
        elif str_strip[0] == '-':
            is_minus = True
            start_index = 1
        else:
            return 0
        res = 0
        for i in range(start_index, len(str_strip)):
            if str_strip[i].isnumeric():
                res = res * 10 + int(str_strip[i])
            else:
                break
        if is_minus:
            res = -res
        min = -2 ** 31
        max = 2 ** 31 - 1
        if res < min:
            res = min
        elif res > max:
            res = max
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi("-91283472332"))
