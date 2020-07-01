class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        if s[0] == '0':
            return 0
        pre, cnt = 1, 1
        for i in range(1, n):
            tmp = cnt
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    tmp = pre
                else:
                    return 0
            elif s[i - 1] == '1':
                tmp = cnt + pre
            elif s[i - 1] == '2' and '1' <= s[i] <= '6':
                tmp = cnt + pre
            pre, cnt = cnt, tmp
        return cnt


assert Solution().numDecodings('1212') == 5
assert Solution().numDecodings('0000') == 0
assert Solution().numDecodings('0010') == 0
assert Solution().numDecodings('1') == 1
assert Solution().numDecodings('12') == 2
assert Solution().numDecodings('226') == 3
assert Solution().numDecodings('01') == 0
assert Solution().numDecodings('10') == 1
assert Solution().numDecodings('230') == 0
