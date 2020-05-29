class Solution(object):
    def isAnagram0(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        look1 = {}
        look2 = {}
        for ch in s:
            look1[ch] = look1.get(ch, 0) + 1
        for ch in t:
            look2[ch] = look2.get(ch, 0) + 1
        if len(s) != len(t):
            return False
        # dict比较可以用==
        return look1 == look2
        # for key in look1:
        #     if look1[key] != look2.get(key):
        #         return False
        # return True

    def isAnagram1(self, s, t):
        return sorted(s) == sorted(t)


print(Solution().isAnagram0("rat", "tar"))
