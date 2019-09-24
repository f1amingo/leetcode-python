class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for (i, num) in enumerate(nums):
            for clist in res[:]:
                res.append(clist + [num])
            res.append([num])
        res.append([])
        return res


print(Solution().subsets([1, 2, 3]))
