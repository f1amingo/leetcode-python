from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(A: List, start: int, end: int):
            end -= 1
            while start < end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1

        n = len(s)
        s_list = [x for x in s]
        i = j = 0
        while i < n:
            j = i + 1
            while j < n and s[j] != ' ':
                j += 1
            reverse(s_list, i, j)
            i = j + 1
        return ''.join(s_list)


print(Solution().reverseWords("Let's take LeetCode contest"))
