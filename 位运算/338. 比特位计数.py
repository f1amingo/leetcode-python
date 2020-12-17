from typing import List


class Solution:
    # 奇数比前一个数多一个1
    # 偶数与右移后相同
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            # 奇数
            if i & 1 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i >> 1]
        return dp

    # 自己琢磨出来的while True...
    # 按4,8,16分段计算
    # def countBits(self, num: int) -> List[int]:
    #     if num < 4:
    #         return [0, 1, 1, 2][:num + 1]
    #     ans = [0, 1, 1, 2] + [0] * (num + 1 - 4)
    #     offset = 4
    #     while True:
    #         for i in range(offset, 2 * offset):
    #             ans[i] = ans[i - offset] + 1
    #             if i == num:
    #                 return ans
    #         offset *= 2

    # O(n*sizeof(inte   ger))
    # 模拟，有点慢
    # def countBits(self, num: int) -> List[int]:
    #     ans = [0] * (num + 1)
    #     for i in range(num + 1):
    #         cur, count = i, 0
    #         while cur != 0:
    #             # 最低位
    #             count += 1 if cur & 1 == 1 else 0
    #             # 右移更新最低位
    #             cur >>= 1
    #         ans[i] = count
    #     return ans


assert Solution().countBits(2) == [0, 1, 1]
assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]
