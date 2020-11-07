from typing import List


# key point: 若数x可以整除子集中最大的数，那么x可以与当前集合，组成新的整除子集
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        # dp[i] 以nums[i]作为最大元素的整除子集的大小
        dp = [1] * n
        # 保存路径，答案需要的是集合，而不是集合的大小
        prev = [-1] * n
        max_len = 1
        max_idx = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
                        if dp[i] > max_len:
                            max_len = dp[i]
                            max_idx = i
        res = []
        i = max_idx
        while i != -1:
            res.append(nums[i])
            i = prev[i]
        return res


print(Solution().largestDivisibleSubset([4, 8, 10, 240]))
print(Solution().largestDivisibleSubset([3, 4, 16, 8]))
print(Solution().largestDivisibleSubset([1, 2, 3]))
print(Solution().largestDivisibleSubset([1, 2, 4, 8]))
