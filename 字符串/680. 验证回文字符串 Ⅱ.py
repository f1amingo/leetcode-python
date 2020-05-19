class Solution:
    # 递归 比较慢
    # def validPalindrome(self, s: str) -> bool:
    #     n = len(s)
    #     if n <= 2:
    #         return True
    #     can_modify = True
    #
    #     def dfs(s, _i, _j):
    #         if _i >= _j:
    #             return True
    #         if s[_i] == s[_j]:
    #             return dfs(s, _i + 1, _j - 1)
    #         nonlocal can_modify
    #         if can_modify:
    #             can_modify = False
    #             return dfs(s, _i + 1, _j) or dfs(s, _i, _j - 1)
    #         return False
    #
    #     return dfs(s, 0, len(s) - 1)

    # 官方题解
    # def validPalindrome(self, s: str) -> bool:
    #     n = len(s)
    #     if n <= 2:
    #         return True
    #     flag = True
    #
    #     def valid(low, high):
    #         while low < high:
    #             if s[low] == s[high]:
    #                 low += 1
    #                 high -= 1
    #             else:
    #                 nonlocal flag
    #                 if flag:
    #                     flag = False
    #                     return valid(low + 1, high) or valid(low, high - 1)
    #                 return False
    #         return True
    #
    #     return valid(0, len(s) - 1)

    # 跑得快的 别人的题解
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                a, b = s[l:r], s[l + 1: r + 1]
                return a == a[::-1] or b == b[::-1]


assert Solution().validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
assert Solution().validPalindrome('aba')
assert Solution().validPalindrome('abca')
assert Solution().validPalindrome('abbca')
