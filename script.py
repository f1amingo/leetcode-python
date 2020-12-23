from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start: int, cur_set: []):
            ans.append(cur_set.copy())
            for i in range(start, n):
                cur_set.append(nums[i])
                dfs(i + 1, cur_set)
                cur_set.pop()

        n = len(nums)
        ans = []
        dfs(0, [])
        return ans


print(Solution().subsets([1, 2, 3]))
