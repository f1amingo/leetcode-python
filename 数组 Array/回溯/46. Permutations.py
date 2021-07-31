from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 确定start位置的元素
        def dfs(start: int):
            if start == n:
                ans.append(nums.copy())
                return
            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                # dfs(i + 1)
                # 下一轮应该确定start + 1而不是i
                dfs(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        ans = []
        n = len(nums)
        dfs(0)
        return ans


print(Solution().permute([1, 2, 3]))
