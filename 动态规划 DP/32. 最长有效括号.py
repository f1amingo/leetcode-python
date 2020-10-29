# dp[i]：以s[i]结尾的序列中最长有效括号的长度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [0] * n
        for i in range(1, n):
            # 有效括号的最右边只能是')'
            if s[i] == ')':
                # 形如'...()'的形式
                if s[i - 1] == '(':
                    dp[i] = dp[max(i - 2, 0)] + 2
                # 形如'...(...)'的形式
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[max(i - dp[i - 1] - 2, 0)] + dp[i - 1] + 2
                res = max(res, dp[i])
        return res


print(Solution().longestValidParentheses("()(())"))
print(Solution().longestValidParentheses(")()())"))
print(Solution().longestValidParentheses("(()"))
