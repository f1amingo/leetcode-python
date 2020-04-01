from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def idx(c):
            return ord(c) - 97

        len_s = len(s)
        len_p = len(p)
        dict_p = [0] * 26
        dict_tmp = [0] * 26
        for c in p:
            dict_p[idx(c)] += 1
        left = 0
        res = []
        for right in range(len_s):
            if right < len_p:
                dict_tmp[idx(s[right])] += 1
                continue
            if dict_p == dict_tmp:
                res.append(left)
            dict_tmp[idx(s[left])] -= 1
            dict_tmp[idx(s[right])] += 1
            left += 1
        if dict_p == dict_tmp:
            res.append(left)
        return res


s = 'abab'
p = 'ab'
print(Solution().findAnagrams(s, p))
