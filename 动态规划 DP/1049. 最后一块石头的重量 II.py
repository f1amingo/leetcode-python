from typing import List


class Solution:
    # 假设有[a,b,c]
    # a, b粉碎，得到新石头a-b
    # a-b与c粉碎，得到c-(a-b) or (a-b)-c
    # 无论大小关系如何，都是可以看做在每个数前添加正负号，然后求和
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        C = total // 2  # 左中位数
        dp = [0] * (C + 1)
        for stone in stones:  # 每个物品都要遍历到
            for c in range(C, stone - 1, -1):
                dp[c] = max(dp[c], dp[c - stone] + stone)
        return total - 2 * dp[-1]  # 前面使用了左中位数，所以这里不会小于0


print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]))
print(Solution().lastStoneWeightII([1, 1, 4, 2, 2]))
print(Solution().lastStoneWeightII([1, 2]))
