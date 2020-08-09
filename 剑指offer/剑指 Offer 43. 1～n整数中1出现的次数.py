class Solution:
    def countDigitOne(self, n: int) -> int:
        low = 0
        high = n // 10
        digit = 1
        cur = n % 10
        res = 0
        while low < n:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low = digit * cur + low
            cur = high % 10
            high = high // 10
            digit *= 10
        return res


print(Solution().countDigitOne(12))
