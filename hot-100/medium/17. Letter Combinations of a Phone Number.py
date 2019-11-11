class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        table = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []

        def dfs(_digits, cur_set):
            if not _digits:
                res.append(cur_set)
                return
            letters = table[int(_digits[0]) - 2]
            for ch in letters:
                dfs(_digits[1:], cur_set + ch)

        dfs(digits, '')

        return res


print(Solution().letterCombinations("234"))
