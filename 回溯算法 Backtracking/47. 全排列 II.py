from typing import List

class Solution:
    # 使用visited数组标记重复
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 枚举位置i可能的元素
        def dfs(i: int):
            if i == n:
                res.append(cur_list.copy())
                return
            for j in range(n):
                # not visited[j-1])
                # 对于重复元素，如果j-1没有被使用说明，是在上一步中被撤销的
                # j-1如果还在使用，说明进入了下一层递归
                if visited[j] or (j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]):
                    continue
                visited[j] = True
                cur_list[i] = nums[j]
                dfs(i + 1)
                visited[j] = False

        res = []
        n = len(nums)
        visited = [False] * n
        cur_list = [0] * n
        nums.sort()
        dfs(0)
        return res

    # 交换法
    # 无法理解
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     def dfs(i: int):
    #         if i == n:
    #             res.append(nums.copy())
    #             return
    #         for j in range(i, n):
    #             # 这个判断不完全，类似[0,0,1,2]的测试用例会错
    #             # 原因在于：假设经过之前交换，当前变成了[2,0,1,0]，i=1，for循环中又会交换nums[1], nums[3]，而这两个都是零，因此就重复了
    #             # if j > i and nums[j] == nums[j - 1]:
    #             if isRepeat(i, j):
    #                 continue
    #             nums[i], nums[j] = nums[j], nums[i]
    #             dfs(i + 1)
    #             nums[i], nums[j] = nums[j], nums[i]
    #
    #     # range(i, j)中间不可以有和nums[j]相同的数
    #     # 无法理解，还是不要用交换法做
    #     def isRepeat(i: int, j: int):
    #         for k in range(i, j):
    #             if nums[k] == nums[j]:
    #                 return True
    #         return False
    #
    #     n = len(nums)
    #     res = []
    #     nums.sort()
    #     dfs(0)
    #     return res


print(Solution().permuteUnique([-1, -1, 0, 0, 1, 1, 2]))
