from typing import List


# 无重复元素，正整数
# 可重复选择
# 所有组合
class Solution:
    # 更加优美的代码
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

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     def dfs(cur_set: List, cur_sum: int, res: List, start: int):
    #         for i in range(start, len(candidates)):
    #             new_sum = cur_sum + candidates[i]
    #             if new_sum == target:
    #                 res.append(cur_set + [candidates[i]])
    #             elif new_sum < target:
    #                 cur_set.append(candidates[i])
    #                 dfs(cur_set, new_sum, res, i)
    #                 cur_set.pop()
    #
    #     res = []
    #     dfs([], 0, res, 0)
    #     return res


print(Solution().combinationSum([5], 6))
