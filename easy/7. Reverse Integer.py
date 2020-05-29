class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        res = 0
        num = abs(x)
        while num:
            res = res * 10 + num % 10
            if res > 2 ** 31 - 1:
                return 0
            num //= 10
        if x < 0:
            res = -res
        return res


print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
print(Solution().reverse(9646324351))
