class Solution:
    # 数学
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1

    # 递归
    # def addDigits(self, num: int) -> int:
    #     if num < 10:
    #         return num
    #     tmp = 0
    #     while num != 0:
    #         num, val = divmod(num, 10)
    #         tmp += val
    #     return self.addDigits(tmp)

    # 循环
    # def addDigits(self, num: int) -> int:
    #     while num >= 10:
    #         tmp = 0
    #         while num != 0:
    #             num, val = divmod(num, 10)
    #             tmp += val
    #         num = tmp
    #     return num


assert Solution().addDigits(38) == 2
