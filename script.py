class Solution:
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


print(Solution().minWindow("A", "A"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
