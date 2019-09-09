class Solution(object):
    # 按部就班
    # def addBinary(self, a, b):
    #     """
    #     :type a: str
    #     :type b: str
    #     :rtype: str
    #     """
    #     size_a = len(a)
    #     size_b = len(b)
    #     size = size_a
    #     if size_a < size_b:
    #         size = size_b
    #     res = ''
    #     carry = 0
    #     for i in range(0, size):
    #         num1 = 0
    #         num2 = 0
    #         if i < size_a:
    #             num1 = int(a[size_a - i - 1])
    #         if i < size_b:
    #             num2 = int(b[size_b - i - 1])
    #         total = num1 + num2 + carry
    #         carry = total // 2
    #         res = str(total % 2) + res
    #     if carry:
    #         res = '1' + res
    #     return res

    # 使用内置函数
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


print(Solution().addBinary('0', '0'))
