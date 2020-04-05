class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contained(d):
            for k in d:
                if d[k] > 0:
                    return False
            return True

        len_s = len(s)
        len_t = len(t)
        if len_t > len_s:
            return ""
        dict_t = {}
        for c in t:
            if c in dict_t:
                dict_t[c] += 1
            else:
                dict_t[c] = 1
        left = right = 0
        start = 0
        end = -1
        while right < len_s:
            if s[right] in dict_t:
                dict_t[s[right]] -= 1
            right += 1
            if contained(dict_t):
                # 开头的字母在t中保证最短
                while left < right:
                    if s[left] in dict_t:
                        if dict_t[s[left]] == 0:
                            break
                        dict_t[s[left]] += 1
                    left += 1
                if end == -1 or end - start > right - left:
                    start = left
                    end = right
                    # left一定在dict_t中
                    dict_t[s[left]] += 1
                    left += 1
        if end == -1:
            return ''
        return s[start: end]


s = 'ab'
t = 'A'
print(Solution().minWindow(s, t))
s = 'ADOBECODEBANC'
t = 'ABC'
print(Solution().minWindow(s, t))
s = 'ab'
t = 'b'
print(Solution().minWindow(s, t))

