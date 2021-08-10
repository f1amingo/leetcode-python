from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start: int, cur_sum: int, cur_list: List):
            if cur_sum == target:
                ans.append(cur_list.copy())
                return
            for i in range(start, n):
                # 当前这个位置，重复的数，只选择第一个
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                new_sum = cur_sum + candidates[i]
                if new_sum > target:
                    break
                cur_list.append(candidates[i])
                dfs(i + 1, new_sum, cur_list)
                cur_list.pop()

        n = len(candidates)
        candidates.sort()
        ans = []
        dfs(0, 0, [])
        return ans


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
