class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(cur_nums, path, cur_target):
            left = 0
            while left < len(cur_nums):
                num = cur_nums[left]
                if num == cur_target:
                    res.append(path + [num])
                    return
                elif num < cur_target:
                    dfs(cur_nums[left + 1:], path + [num], cur_target - num)
                    left += 1
                    # 找到下一位不相同的数，去重
                    while left < len(cur_nums) and cur_nums[left] == cur_nums[left - 1]:
                        left += 1
                else:
                    break

        dfs(candidates, [], target)

        return res


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
