class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == 0 or k >= n:
            return '0'
        stk = []
        for digit in num:
            while stk and stk[-1] > digit and k != 0:
                stk.pop()
                k -= 1
            stk.append(digit)
        res = ''.join(stk)
        # 去除前导零
        res = res.lstrip('0')
        # 没有删够k个数
        if k != 0:
            res = res[:-k]
        # 空str时，返回‘0’
        return res if res else '0'


print(Solution().removeKdigits("10", 1))
print(Solution().removeKdigits("123456789", 3))
print(Solution().removeKdigits("10200", 1))
