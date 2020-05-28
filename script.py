import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        most_c = ''
        ans = 0
        found = collections.defaultdict(int)
        while right < len(s):
            found[s[right]] += 1
            # 注意等于：更新为最新进来的元素
            # 防止左移把以前的most_c移出去，导致while出错
            if found[s[right]] >= found[most_c]:
                most_c = s[right]
            while right - left + 1 > k + found[most_c]:
                found[s[left]] -= 1
                left += 1
            right += 1
            ans = max(ans, right - left)
        return ans


print(Solution().characterReplacement("BAAA", 0))
print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("AABABBA", 1))
