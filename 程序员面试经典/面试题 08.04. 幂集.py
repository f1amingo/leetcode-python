from typing import List


class Solution:

    # 直接生成法
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [r + [num] for r in res]
            # for i in range(len(res)):
            #     res.append(res[i] + [num])
        return res

    # 回溯
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     def dfs(start: int, cur_list: List):
    #         # 一开始就append
    #         res.append(cur_list.copy())
    #         if start >= n:
    #             return
    #         for i in range(start, n):
    #             cur_list.append(nums[i])
    #             # 关键：下一轮只能选取i之后的数，避免重复
    #             dfs(i + 1, cur_list)
    #             cur_list.pop()
    #
    #     n = len(nums)
    #     res = []
    #     dfs(0, [])
    #     return res


print(Solution().subsets([1, 2, 3]))
