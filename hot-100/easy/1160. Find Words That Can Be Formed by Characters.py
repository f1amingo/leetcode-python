from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for s in words:
            chars_copy = chars
            is_good = True
            for c in s:
                find_i = chars_copy.find(c)
                if find_i == -1:
                    is_good = False
                    break
                chars_copy = chars_copy[:find_i] + chars_copy[find_i + 1:]
            if is_good:
                res += len(s)
        return res


words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(Solution().countCharacters(words, chars))
