from typing import List


class Solution:
    # 拼接数组 频繁申请空间
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     if n == 0:
    #         return []
    #     if n == 1:
    #         return [nums]
    #     ans = []
    #
    #     def dfs(tmp, cur_nums):
    #         if not cur_nums:
    #             ans.append(tmp)
    #             return
    #         for i in range(len(cur_nums)):
    #             dfs(tmp + [cur_nums[i]], cur_nums[:i] + cur_nums[i + 1:])
    #
    #     dfs([], nums)
    #     return ans

    # 利用交换将候选数字换到前面
    # 结果非字典序
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     ans = []
    #
    #     def backtrack(depth=0):
    #         if depth == n:
    #             ans.append(nums[:])
    #             return
    #         这里从depth开始遍历，depth这个位置为下一个候选位，左边已确定，右边待选择
    #         for i in range(depth, n):
    #             nums[i], nums[depth] = nums[depth], nums[i]
    #             backtrack(depth + 1)
    #             nums[depth], nums[i] = nums[i], nums[depth]
    #
    #     backtrack()
    #     return ans

    # 上一种方法使用used数组
    # 结果为字典序
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = [False] * n
        tmp = []

        def backtrack(depth=0):
            if depth == n:
                ans.append(tmp[:])
                return
            # 这里要对整个数组进行遍历
            for i in range(0, n):
                if not used[i]:
                    used[i] = True
                    tmp.append(nums[i])
                    backtrack(depth + 1)
                    used[i] = False
                    tmp.pop()

        backtrack()
        return ans


print(Solution().permute([1, 2, 3]))
