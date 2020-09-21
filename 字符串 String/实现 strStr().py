class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size_a = len(haystack)
        size_b = len(needle)
        if size_b == 0:
            return 0
        if size_a == 0:
            return -1
        p2 = 0
        for p1 in range(0, size_a):
            if haystack[p1] == needle[p2]:
                if p2 == size_b - 1:
                    return p1 - p2
                else:
                    p2 += 1
            else:
                p2 = 0
        return -1


print(Solution().strStr("mississippi",
                        "issip"))
