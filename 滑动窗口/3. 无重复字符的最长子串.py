class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dict记个数
        # len_s = len(s)
        # if len_s < 2:
        #     return len_s
        # ans = 0
        # left = 0
        # dict_s = {}
        # for right in range(len_s):
        #     while dict_s.get(s[right], 0) > 0:
        #         dict_s[s[left]] -= 1
        #         left += 1
        #     dict_s[s[right]] = 1
        #     ans = max(right - left + 1, ans)
        # return ans

        # 记索引
        len_s = len(s)
        if len_s < 2:
            return len_s
        ans = 0
        left = 0
        dict_s = {}
        for right in range(len_s):
            if dict_s.get(s[right], -1) != -1:
                left = max(dict_s[s[right]] + 1, left)
            dict_s[s[right]] = right
            ans = max(right - left + 1, ans)
        return ans


print(Solution().lengthOfLongestSubstring("abba"))
