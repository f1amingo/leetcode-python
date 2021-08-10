from typing import List


# 结果不重复
# 无序
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start: int, cur_sum: int, cur_list: List):
            if cur_sum == target:
                ans.append(cur_list.copy())
                return
            for i in range(start, n):
                new_sum = cur_sum + candidates[i]
                if new_sum > target:
                    break
                cur_list.append(candidates[i])
                dfs(i, new_sum, cur_list)
                cur_list.pop()

        candidates.sort()
        n = len(candidates)
        ans = []
        dfs(0, 0, [])
        return ans


print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))
print(Solution().combinationSum([2], 1))
