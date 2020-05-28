import collections


class Solution:
    # 官方
    # def characterReplacement(self, s: str, k: int) -> int:
    #     len_s = len(s)
    #     if len_s < 2:
    #         return len_s
    #     cur_dict = [0] * 26
    #     left = 0
    #     max_count = 0
    #     ans = 0
    #     for right in range(len_s):
    #         dict_idx = ord(s[right]) - ord('A')
    #         cur_dict[dict_idx] += 1
    #         max_count = max(max_count, cur_dict[dict_idx])
    #         if right - left + 1 > max_count + k:
    #             cur_dict[ord(s[left]) - ord('A')] -= 1
    #             left += 1
    #         ans = max(ans, right - left + 1)
    #     return ans

    # 重写
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, ans, most_c = 0, 0, 0, ''
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


s = 'ABBB'
k = 2
print(Solution().characterReplacement(s, k))
