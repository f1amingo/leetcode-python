class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def dfs(cur_set, index):
            res.append(cur_set)
            left = index
            while left < len(nums):
                dfs(cur_set + [nums[left]], left + 1)
                left += 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1

        dfs([], 0)

        return res


print(Solution().subsetsWithDup([1, 2, 2]))
