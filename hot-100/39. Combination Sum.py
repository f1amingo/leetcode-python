class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        # 不一定要排序
        candidates.sort()

        # index的理解：先选了后一个数就不能再选前一个数了
        def dfs(cur_list, cur_target, index):
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num == cur_target:
                    res.append(cur_list + [num])
                elif num < cur_target:
                    dfs(cur_list + [num], cur_target - num, i)
                else:  # 有序的则可以跳过后面的
                    break

        dfs([], target, 0)

        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
