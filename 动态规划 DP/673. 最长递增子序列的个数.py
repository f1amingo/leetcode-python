from typing import List


class Solution:
    # 两个数组
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        L = [1] * n  # 以A[i]结尾的最长递增子数组长度
        C = [1] * n  # 以A[i]结尾的最长递增子数组数目
        maxL = 1
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if L[i] >= L[j]:
                        L[j] = L[i] + 1
                        C[j] = C[i]
                    elif L[i] + 1 == L[j]:
                        C[j] += C[i]
            maxL = max(maxL, L[j])
        count = 0
        for i in range(n):
            if L[i] == maxL:
                count += C[i]
        return count


assert Solution().findNumberOfLIS([1, 3, 5, 4, 7]) == 2
assert Solution().findNumberOfLIS([2, 2, 2, 2, 2]) == 5
