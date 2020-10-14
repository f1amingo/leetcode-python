from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(cur_set: List, cur_sum: int, res: List, start: int):
            for i in range(start, len(candidates)):
                new_sum = cur_sum + candidates[i]
                if new_sum == target:
                    res.append(cur_set + [candidates[i]])
                elif new_sum < target:
                    cur_set.append(candidates[i])
                    dfs(cur_set, new_sum, res, i)
                    cur_set.pop()

        res = []
        dfs([], 0, res, 0)
        return res


print(Solution().combinationSum([5], 6))
