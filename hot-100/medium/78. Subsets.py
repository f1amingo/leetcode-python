class Solution(object):
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     for (i, num) in enumerate(nums):
    #         for clist in res[:]:
    #             res.append(clist + [num])
    #         res.append([num])
    #     res.append([])
    #     return res

    def subsets(self, nums):
        res = []

        def dfs(nums, index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i + 1, path + [nums[i]])

        dfs(nums, 0, [])
        return res


print(Solution().subsets([1, 2, 3]))
