class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(index, sub, cur_k):
            if cur_k == 0:
                res.append(sub)
                return
            for i in range(index, n):
                dfs(i + 1, sub + [i + 1], cur_k - 1)

        dfs(0, [], k)
        return res


print(Solution().combine(4, 2))
