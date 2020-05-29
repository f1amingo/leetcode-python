class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def dfs(cur_nums, path):
            if not cur_nums:
                res.append(path)
                return
            left = 0
            while left < len(cur_nums):
                dfs(cur_nums[:left] + cur_nums[left + 1:], path + [cur_nums[left]])
                left += 1
                while left < len(cur_nums) and cur_nums[left] == cur_nums[left - 1]:
                    left += 1

        dfs(nums, [])
        return res


print(Solution().permuteUnique([1, 1, 2]))
