class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        com_str = strs[0]
        for s in strs:
            last_index = len(com_str)
            if len(s) < len(com_str):
                last_index = len(s)
            for i in range(0, last_index):
                if s[i] != com_str[i]:
                    last_index = i
                    break
            com_str = s[: last_index]
            if com_str == '':
                break
        return com_str


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(['ca', 'a']))
