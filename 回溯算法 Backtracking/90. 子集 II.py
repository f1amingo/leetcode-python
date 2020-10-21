from typing import List


# 这类组合问题，首先要排序，然后不要选之前的数，就不会重复
# 结果中每一项都是非递减序列
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            res.append(cur_list.copy())
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                cur_list.append(nums[j])
                dfs(j + 1)
                cur_list.pop()

        res = []
        cur_list = []
        n = len(nums)
        nums.sort()
        dfs(0)
        return res


print(Solution().subsetsWithDup([1, 2, 2]))
