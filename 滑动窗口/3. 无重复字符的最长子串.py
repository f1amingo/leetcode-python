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

    # 记索引
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     len_s = len(s)
    #     if len_s < 2:
    #         return len_s
    #     ans = 0
    #     left = 0
    #     dict_s = {}
    #     for right in range(len_s):
    #         if dict_s.get(s[right], -1) != -1:
    #             left = max(dict_s[s[right]] + 1, left)
    #         dict_s[s[right]] = right
    #         ans = max(right - left + 1, ans)
    #     return ans


print(Solution().lengthOfLongestSubstring("abba"))
