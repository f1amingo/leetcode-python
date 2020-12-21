import collections
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = collections.Counter(wordDict)
        n = len(s)
        dp = [True] + [False] * n
        for i in range(n):
            for j in range(i, -1, -1):
                dp[i + 1] = s[j:i + 1] in word_dict and dp[j]
                if dp[i + 1]:
                    break
        return dp[-1]


assert Solution().wordBreak('leetcode', ["leet", "code"])
assert Solution().wordBreak('applepenapple', ["apple", "pen"])
assert not Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"])
