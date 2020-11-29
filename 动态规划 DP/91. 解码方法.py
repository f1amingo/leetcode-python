class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        # 前导零不合法
        if s[0] == '0':
            return 0
        n = len(s)
        pre, cur = 1, 1
        for i in range(1, n):
            num = int(s[i - 1:i + 1])
            # s[i]为零，只能联合解码，但是s[i-1]s[i]又不合法
            if s[i] == '0' and num > 26:
                return 0
            if num == 0:
                # 连续两个0
                return 0
            elif num < 10 or num > 26:
                # num < 10: 01到09，不能有前导零，s[i]独自解码
                # num > 26: 不再有意义，s[i]独自解码
                tmp = cur
            elif num == 10 or num == 20:
                # s[i]为0，s[i-1]s[i]联合解码
                tmp = pre
            elif num <= 26:
                # s[i]可以独自解码
                # s[i-1]s[i]可以联合解码
                tmp = cur + pre
            pre, cur = cur, tmp
        return cur


assert Solution().numDecodings("301") == 0  # 中间不合法的0
assert Solution().numDecodings("230") == 0  # 单独一个0无法解码
assert Solution().numDecodings("1201234") == 3
assert Solution().numDecodings("01") == 0  # 前导零不合法
assert Solution().numDecodings("10011") == 0  # 连续两个0无效
assert Solution().numDecodings("2101") == 1  # 1,2,...,9,10只有一种解法
assert Solution().numDecodings('10') == 1
assert Solution().numDecodings('12') == 2
assert Solution().numDecodings('226') == 3
assert Solution().numDecodings('0') == 0
assert Solution().numDecodings('1') == 1
assert Solution().numDecodings('2') == 1