class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        # 保存进位
        res, carry = '', 0
        while i >= 0 or j >= 0:
            digit = carry
            if i >= 0:
                digit += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                digit += ord(num2[j]) - ord('0')
                j -= 1
            carry, digit = digit // 10, digit % 10
            res = str(digit) + res
        # 这里容易忘记
        if carry:
            res = '1' + res
        return res


print(Solution().addStrings('1', '9'))
