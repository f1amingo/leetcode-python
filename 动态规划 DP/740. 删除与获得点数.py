from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = max(nums)  # 最大的数
        dp = [0] * (n + 1)  # 多申请1空间，避免之后计算偏移，以及边界处理
        A = [0] * (n + 1)
        for num in nums:  # 构造新的存储结构
            A[num] += 1
        dp[1] = A[1]  # 0, 1需要单独处理
        for i in range(2, n + 1):  # 可以从2开始遍历
            dp[i] = max(A[i] * i + dp[i - 2], dp[i - 1])
        return dp[-1]


print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
