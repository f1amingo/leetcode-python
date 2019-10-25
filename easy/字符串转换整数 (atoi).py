class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        is_minus = False
        left = 0
        for i, ch in enumerate(str):
            if ch != ' ':
                left = i
                break
        if str[left] == '-' or str[left] == '+':
            is_minus = True if str[left] == '-' else False
            left += 1
        res = 0
        while left < len(str):
            if not str[left].isdigit():
                break
            res = res * 10 + int(str[left])
            left += 1
        if res != 0 and is_minus:
            res = -res
        if res < INT_MIN:
            res = INT_MIN
        elif res > INT_MAX:
            res = INT_MAX
        return res


print(Solution().myAtoi("-"))
