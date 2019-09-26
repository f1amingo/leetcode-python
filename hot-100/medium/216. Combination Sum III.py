class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(cur_k, cur_n, index, path):
            for i in range(index, 10):
                if cur_k == 1 and cur_n == i:
                    res.append(path + [i])
                    return
                elif cur_k > 0 and cur_n > i:
                    dfs(cur_k - 1, cur_n - i, i + 1, path + [i])
                else:
                    return

        dfs(k, n, 1, [])
        return res


print(Solution().combinationSum3(3, 9))
