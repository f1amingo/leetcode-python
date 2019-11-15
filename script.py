from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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


print(Solution().letterCombinations(''))
print(Solution().letterCombinations("23"))
