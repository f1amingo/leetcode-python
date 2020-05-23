class Solution:
    # My solution
    # def minWindow(self, s: str, t: str) -> str:
    #     def contained(d):
    #         for k in d:
    #             if d[k] > 0:
    #                 return False
    #         return True
    #
    #     len_s = len(s)
    #     len_t = len(t)
    #     if len_t > len_s:
    #         return ""
    #     dict_t = {}
    #     for c in t:
    #         if c in dict_t:
    #             dict_t[c] += 1
    #         else:
    #             dict_t[c] = 1
    #     left = right = 0
    #     start = 0
    #     end = -1
    #     while right < len_s:
    #         if s[right] in dict_t:
    #             dict_t[s[right]] -= 1
    #         right += 1
    #         if contained(dict_t):
    #             # 开头的字母在t中保证最短
    #             while left < right:
    #                 if s[left] in dict_t:
    #                     if dict_t[s[left]] == 0:
    #                         break
    #                     dict_t[s[left]] += 1
    #                 left += 1
    #             if end == -1 or end - start > right - left:
    #                 start = left
    #                 end = right
    #                 # left一定在dict_t中
    #                 dict_t[s[left]] += 1
    #                 left += 1
    #     if end == -1:
    #         return ''
    #     return s[start: end]

    # 参考别人写法
    # 改进使用valid来判断是否包含t
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        needs = {}
        # 各字母需要出现次数
        for c in t:
            needs[c] = needs.get(c, 0) + 1
        left = right = 0
        # valid个字母的出现次数不满足
        # valid==0说明当前窗口包含t
        valid = len(needs)
        start, end = -1, -1
        while right < len(s):
            # 移动right
            if s[right] in needs:
                needs[s[right]] -= 1
                # 该字母已经满足
                if needs[s[right]] == 0:
                    valid -= 1
            while valid == 0:
                # 首先更新ans
                if start == -1 or right - left < end - start:
                    start, end = left, right
                if s[left] in needs:
                    # 左边界之前满足
                    if needs[s[left]] == 0:
                        valid += 1
                    needs[s[left]] += 1
                left += 1
            right += 1
        return s[start:end + 1]


s = 'ab'
t = 'A'
print(Solution().minWindow(s, t))
s = 'ADOBECODEBANC'
t = 'ABC'
print(Solution().minWindow(s, t))
s = 'ab'
t = 'b'
print(Solution().minWindow(s, t))

