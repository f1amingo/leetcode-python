class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        len_s = len(s)
        if len_s < 2:
            return len_s
        cur_dict = [0] * 26
        left = 0
        max_count = 0
        ans = 0
        for right in range(len_s):
            dict_idx = ord(s[right]) - ord('A')
            cur_dict[dict_idx] += 1
            max_count = max(max_count, cur_dict[dict_idx])
            if right - left + 1 > max_count + k:
                cur_dict[ord(s[left]) - ord('A')] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


s = 'ABBB'
k = 2
print(Solution().characterReplacement(s, k))
