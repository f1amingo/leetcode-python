from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(start: int):
            if start == n:
                ans.append(nums.copy())
                return
            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                dfs(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        n = len(nums)
        ans = []
        dfs(0)
        return ans


print(Solution().permute([1, 2, 3]))
