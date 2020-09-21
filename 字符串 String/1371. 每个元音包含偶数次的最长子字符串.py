class Solution:
    # 官方题解
    # def findTheLongestSubstring(self, s: str) -> int:
    #     n = len(s)
    #     pos = [-1] * (1 << 5)
    #     ans, status = 0, 0
    #     pos[0] = 0
    #     for i, c in enumerate(s):
    #         if c == 'a':
    #             status ^= (1 << 0)
    #         elif c == 'e':
    #             status ^= (1 << 1)
    #         elif c == 'i':
    #             status ^= (1 << 2)
    #         elif c == 'o':
    #             status ^= (1 << 3)
    #         elif c == 'u':
    #             status ^= (1 << 4)
    #         if pos[status] >= 0:
    #             ans = max(ans, i + 1 - pos[status])
    #         else:
    #             pos[status] = i + 1
    #     return ans

    def findTheLongestSubstring(self, s: str) -> int:
        vowel = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        pos, prefix, ans = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in vowel:
                prefix ^= vowel[c]
            if prefix in pos:
                ans = max(ans, i - pos[prefix])
            else:
                pos[prefix] = i
        return ans


print(Solution().findTheLongestSubstring("eleetminicoworoep"))
print(Solution().findTheLongestSubstring("leetcodeisgreat"))
