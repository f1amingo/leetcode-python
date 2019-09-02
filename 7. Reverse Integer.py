# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#             """
#         if x < -2 ** 31 or x > (2 ** 31 - 1):
#             return 0
#         isNegative = x < 0
#         x = abs(x)
#         str_x = str(x)[::-1]
#         if isNegative:
#             res = -int(str_x)
#         else:
#             res = int(str_x)
#         if res < -2 ** 31 or res > (2 ** 31 - 1):
#             return 0
#         return res


# class Solution(object):
#     def reverse(self, x):
#         if x < -2 ** 31 or x > (2 ** 31 - 1):
#             return 0
#         isNegative = x < 0
#         digit_arr = []
#         x = abs(x)
#         while x:
#             digit_arr.append(x % 10)
#             x = int(x / 10)
#         base = 1
#         res = 0
#         for i in range(len(digit_arr) - 1, -1, -1):
#             res = res + base * digit_arr[i]
#             base *= 10
#         if isNegative:
#             res = -res
#         if res < -2 ** 31 or res > (2 ** 31 - 1):
#             return 0
#         return res


class Solution(object):
    def reverse(self, x):
        if x < -2 ** 31 or x > (2 ** 31 - 1):
            return 0
        isNegative = x < 0
        digit_arr = []
        x = abs(x)
        res = 0
        while x:
            this_digit = x % 10
            digit_arr.append(this_digit)
            x = int(x / 10)
            res = res * 10 + this_digit
        if isNegative:
            res = -res
        if res < -2 ** 31 or res > (2 ** 31 - 1):
            return 0
        return res


if __name__ == "__main__":
    solution = Solution()
    res = solution.reverse(-123)
    print(res)
