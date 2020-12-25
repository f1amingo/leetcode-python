import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        lt = rt = 0
        found = collections.defaultdict(int)
        while rt < n:
            found[s[rt]] += 1
            if found[s[rt]] == 1:
                ans = max(ans, rt - lt + 1)
            while found[s[rt]] != 1 and lt < rt:
                found[s[lt]] -= 1
                lt += 1
            rt += 1
        return ans


assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
assert Solution().lengthOfLongestSubstring('bbbbb') == 1
assert Solution().lengthOfLongestSubstring('pwwkew') == 3
