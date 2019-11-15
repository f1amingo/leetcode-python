from typing import List


class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
        # if not digits:
        #     return []
        # table = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # res = []
        #
        # def dfs(_digits, cur_set):
        #     if not _digits:
        #         res.append(cur_set)
        #         return
        #     letters = table[int(_digits[0]) - 2]
        #     for ch in letters:
        #         dfs(_digits[1:], cur_set + ch)
        #
        # dfs(digits, '')
        #
        # return res

        letter_table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = []
        if not digits:
            return ans

        def dfs(cur, _digits):
            if not _digits:
                ans.append(cur)
                return
            letters = letter_table[_digits[0]]
            for letter in letters:
                dfs(cur + letter, _digits[1:])

        dfs('', digits)
        return ans


print(Solution().letterCombinations("234"))
