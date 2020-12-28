class Solution:
    # 二分法
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0
        isNegative = True if dividend ^ divisor < 0 else False
        dividend, divisor = abs(dividend), abs(divisor)
        ans = dividend
        if divisor != 1:
            ans = 0
            while dividend >= divisor:
                cur, tmp = divisor, 1
                while cur + cur < dividend:
                    cur += cur
                    tmp = tmp + tmp  # 每次翻两倍
                ans += tmp
                dividend = dividend - cur
        ans = -ans if isNegative else ans
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        return ans if MIN <= ans <= MAX else MAX

    # 暴力超时
    # def divide(self, dividend: int, divisor: int) -> int:
    #     if divisor == 0:
    #         return 0
    #     isNegative = True if dividend ^ divisor < 0 else False
    #     dividend, divisor = abs(dividend), abs(divisor)
    #     ans, cur = 0, 0
    #     while cur < dividend:
    #         cur += divisor
    #         ans += 1
    #     if cur > dividend:
    #         ans -= 1
    #     return -ans if isNegative else ans


assert Solution().divide(2147483647, 2) == 1073741823
assert Solution().divide(-2147483648, -1) == 2147483647
assert Solution().divide(1, 1) == 1
assert Solution().divide(10, 3) == 3
assert Solution().divide(7, -3) == -2
