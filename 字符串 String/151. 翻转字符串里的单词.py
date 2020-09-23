from typing import List


class Solution:
    # 把每个单词放到一个栈里
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = j = 0
        stk = []
        while i < n:
            if s[i] != ' ':
                j = i + 1
                while j < n and s[j] != ' ':
                    j += 1
                stk.append(s[i:j])
                i = j + 1  # !!!!!不要一天到晚写无限循环可以吗
            else:
                i += 1
        stk.reverse()
        return ' '.join(stk)

    # 整个reverse，再逐个单词reverse
    # def reverseWords(self, s: str) -> str:
    #     def reverse(A: List, start: int, end: int):
    #         while start < end:
    #             A[start], A[end] = A[end], A[start]
    #             start += 1
    #             end -= 1
    #
    #     s = s.strip()
    #     n = len(s)
    #     arr = []
    #     # 预处理掉多余的空格
    #     for i in range(n):
    #         if i > 0 and s[i] == ' ' and s[i - 1] == ' ':
    #             continue
    #         arr.append(s[i])
    #     # 整体reverse
    #     reverse(arr, 0, len(arr) - 1)
    #     # reverse单词
    #     i = j = 0
    #     while i < len(arr):
    #         if arr[i] != ' ':
    #             j = i + 1
    #             while j < len(arr) and arr[j] != ' ':
    #                 j += 1
    #             reverse(arr, i, j - 1)
    #             i = j + 1
    #         else:
    #             i += 1
    #     return ''.join(arr)

    # def reverseWords(self, s: str) -> str:
    #     # split()会将多个空格视为一个
    #     return ' '.join(reversed(s.split()))

    # my solution
    # def reverseWords(self, s: str) -> str:
    #     s_list = s.split(' ')
    #     # s_list = [w for w in s_list if w != '']
    #     s_list.reverse()
    #     return ' '.join(s_list)


print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world!  "))
print(Solution().reverseWords("a good   example"))
