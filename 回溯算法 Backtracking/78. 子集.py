from typing import List


class Solution:

    # 迭代
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
    #     for num in nums:
    #         res = res + [r + [num] for r in res]
    #     return res

    # 递归
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            res.append(cur_list.copy())
            # 循环自带递归边界判断，i小于n才可能进入循环
            for j in range(i, n):
                # 把[i]入栈
                cur_list.append(nums[j])
                # 下一个数只能选j之后的
                dfs(j + 1)
                # 复原
                cur_list.pop()

        res = []
        n = len(nums)
        cur_list = []
        dfs(0)
        return res


print(Solution().subsets([1, 2, 3]))
