class Solution(object):
    # 暴力 超时
    def firstUniqChar0(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        for i in range(n):
            is_unique = True
            for j in range(n):
                if s[i] == s[j] and i != j:
                    is_unique = False
                    break
            if is_unique:
                return i
        return -1

    # hash map
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        look = {}
        for ch in s:
            look[ch] = look.get(ch, 0) + 1
        for (i, ch) in enumerate(s):
            if look[ch] == 1:
                return i
        return -1

    # 简化代码
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {c: s.count(c) for c in set(s)}
        for i, j in enumerate(s):
            if lookup[j] == 1:
                return i
        return -1


print(Solution().firstUniqChar("cc"))
print(Solution().firstUniqChar("c"))
print(Solution().firstUniqChar("aadadaad"))
