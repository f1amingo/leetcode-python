class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 直觉方法
        # res = []
        # for i in range(num + 1):
        #     bin_num = bin(i)
        #     one_count = 0
        #     for ch in bin_num[2:]:
        #         if ch == '1':
        #             one_count += 1
        #     res.append(one_count)
        # return res

        # 动态规划
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


print(Solution().countBits(2))
print(Solution().countBits(5))
