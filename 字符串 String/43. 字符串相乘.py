from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def singleMultiply(digit: str, num: str, zero_count: int) -> List[int]:
            if digit == '0':
                return [0]
            digit_int = ord(digit) - ord('0')
            production = [0] * zero_count
            carry = 0
            for i in range(len(num) - 1, -1, -1):
                tmp = digit_int * (ord(num[i]) - ord('0')) + carry
                carry, a = divmod(tmp, 10)
                production.append(a)
            if carry:
                production.append(carry)
            return production

        def add(a: List[int], b: List[int]) -> List[int]:
            _sum = []
            m, n = len(a), len(b)
            i = j = 0
            carry = 0
            while i < m or j < n:
                d1 = a[i] if i < m else 0
                d2 = b[j] if j < n else 0
                carry, digit = divmod(d1 + d2 + carry, 10)
                _sum.append(digit)
                i += 1
                j += 1
            if carry:
                _sum.append(carry)
            return _sum

        # 保证num1更短
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        res = [0]
        len1 = len(num1)
        for i in range(len1):
            res = add(res, singleMultiply(num1[len1 - i - 1], num2, i))
        res.reverse()
        res = [str(x) for x in res]
        return ''.join(res)


assert Solution().multiply('123', '456') == '56088'
assert Solution().multiply('2', '3') == '6'
