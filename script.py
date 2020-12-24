from typing import List


# 无重复元素，正整数
# 可重复选择
# 所有组合
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start: int, t: int, cur_set: List):
            if t <= 0:
                if t == 0:
                    ans.append(cur_set.copy())
                return
            for i in range(start, n):
                cur_set.append(candidates[i])
                dfs(i, t - candidates[i], cur_set)
                cur_set.pop()

        n = len(candidates)
        ans = []
        dfs(0, target, [])
        return ans


print(Solution().combinationSum([2, 3, 5], 8))
print(Solution().combinationSum([2, 3, 6, 7], 7))
