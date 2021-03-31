import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        lt, rt = 0, 0
        found = collections.defaultdict(int)
        while rt < n:
            found[s[rt]] += 1
            while found[s[rt]] > 1:
                found[s[lt]] -= 1
                lt += 1
            ans = max(ans, rt - lt + 1)
            rt += 1
        return ans


assert Solution().lengthOfLongestSubstring('') == 0
assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
