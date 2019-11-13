class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def dfs(cur_set, left, right):
            if len(cur_set) == 2 * n:
                ans.append(cur_set)
                return
            if left < n:
                dfs(cur_set + '(', left + 1, right)
            if right < left:
                dfs(cur_set + ')', left, right + 1)

        dfs('', 0, 0)
        return ans


print(Solution().generateParenthesis(3))
