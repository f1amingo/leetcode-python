class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # python空数组False
        if not s:
            return 0
        left = 0
        lookup = set()
        max_len = 0
        cur_len = 0
        for (i, char) in enumerate(s):
            # set中是否存在
            if char in lookup:
                while char in lookup:
                    lookup.remove(s[left])
                    left += 1
                    cur_len -= 1
            lookup.add(char)
            cur_len += 1
            if max_len < cur_len:
                max_len = cur_len
        return max_len


print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring(''))
