class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        nums.sort()

        def dfs(cur_target, count, path):
            for i in nums:
                if i == cur_target:
                    res.append(path + [i])
                    return count + 1
                elif cur_target > i:
                    count = dfs(cur_target - i, count, path + [i])
                else:
                    return count
            return count

        count = dfs(target, 0, [])
        print(res)
        return count


print(Solution().combinationSum4([4, 2, 1], 32))
