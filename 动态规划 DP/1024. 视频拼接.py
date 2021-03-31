from typing import List


# 区间类问题草稿可以画线段，而不是用数字
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [999] * (T + 1)
        # 初始化
        dp[0] = 0
        for i in range(T + 1):
            for start, end in clips:
                if start <= i <= end:
                    dp[i] = min(dp[i], dp[start] + 1)
        return -1 if dp[-1] == 999 else dp[-1]


assert Solution().videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10) == 3
assert Solution().videoStitching([[0, 1], [1, 2]], 5) == -1
