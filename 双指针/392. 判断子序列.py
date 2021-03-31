class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m


assert not Solution().isSubsequence('a', '')
assert Solution().isSubsequence('a', 'a')
assert Solution().isSubsequence('abc', 'abc')
assert Solution().isSubsequence('abc', 'ahbgdc')
