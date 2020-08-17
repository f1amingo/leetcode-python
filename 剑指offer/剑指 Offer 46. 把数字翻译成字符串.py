class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        a, b = 0, num % 10
        pre, cnt = 1, 1
        num //= 10
        while num:
            a = num % 10
            # 注意递推
            tmp = cnt
            if a != 0 and 10 * a + b < 26:
                # 递推
                tmp += pre
            cnt, pre = tmp, cnt
            b = a
            num //= 10
        return cnt


print(Solution().translateNum(12258))
