class Solution:

    def reverseWords(self, s: str) -> str:
        # split()会将多个空格视为一个
        return ' '.join(reversed(s.split()))

    # my solution
    # def reverseWords(self, s: str) -> str:
    #     s_list = s.split(' ')
    #     # s_list = [w for w in s_list if w != '']
    #     s_list.reverse()
    #     return ' '.join(s_list)


print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world!  "))
print(Solution().reverseWords("a good   example"))
