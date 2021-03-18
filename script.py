from typing import List


# 1.可重复，相等也算递增
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            if len(cur) > 1:
                ans.append(cur.copy())
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                if nums[j] >= cur[-1]:
                    cur.append(nums[j])
                    dfs(j + 1)
                    cur.pop()

        ans = []
        cur = []
        n = len(nums)
        for i in range(n):
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
        return ans


print(Solution().findSubsequences([1, 1, 1, 1]))
# print(Solution().findSubsequences([4, 6, 7, 7]))
