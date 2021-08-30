from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, cur_list, cur_sum):
            if cur_sum == n and len(cur_list) == k:
                ans.append(cur_list.copy())
                return
            if cur_sum >= n or len(cur_list) >= k:
                return
            for i in range(start, 10):
                new_sum = cur_sum + i
                # 提前跳出
                if new_sum > n:
                    break
                cur_list.append(i)
                dfs(i + 1, cur_list, new_sum)
                cur_list.pop()

        ans = []
        dfs(1, [], 0)
        return ans


print(Solution().combinationSum3(3, 7))
