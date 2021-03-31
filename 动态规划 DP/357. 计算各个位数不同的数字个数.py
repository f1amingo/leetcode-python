class Solution:

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 9
        ans = dp[0] + dp[1]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (10 - i + 1)
            ans += dp[i]
        return ans

    # def countNumbersWithUniqueDigits(self, n: int) -> int:
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return 10
    #     ans = 10
    #     cur_sum = 9
    #     remain_digit = 9
    #     for i in range(1, n):
    #         cur_sum *= remain_digit
    #         ans += cur_sum
    #         remain_digit -= 1
    #     return ans


assert Solution().countNumbersWithUniqueDigits(1) == 10
assert Solution().countNumbersWithUniqueDigits(2) == 91
