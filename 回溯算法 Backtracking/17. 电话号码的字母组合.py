from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i: int, cur_list: []):
            if i == n:
                ans.append(''.join(cur_list))
                return
            for c in mapping[digits[i]]:
                cur_list.append(c)
                dfs(i + 1, cur_list)
                cur_list.pop()

        if not digits:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        n, ans = len(digits), []
        dfs(0, [])
        return ans


print(Solution().letterCombinations('23'))
