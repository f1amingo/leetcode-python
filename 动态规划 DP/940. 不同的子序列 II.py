class Solution(object):
    def distinctSubseqII(self, S):
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i

        return (dp[-1] - 1) % (10 ** 9 + 7)


assert Solution().distinctSubseqII('aaa') == 3
assert Solution().distinctSubseqII('abc') == 7
assert Solution().distinctSubseqII('aba') == 6
