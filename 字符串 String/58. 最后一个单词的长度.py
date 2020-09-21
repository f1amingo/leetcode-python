class Solution:

    # more clean code
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >= 0 and s[end] == ' ':
            end -= 1
        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1
        return end - start

    # 字符串可能以空格结尾 "Hello "
    # 1.从末尾开始找到第一个非空字符串，下标end
    # 2.从end开始找到第一个空格
    # def lengthOfLastWord(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     n = len(s)
    #     start = end = -1
    #     for i in range(n - 1, -1, -1):
    #         if s[i] != ' ':
    #             end = i
    #             break
    #     for i in range(end - 1, -1, -1):
    #         if s[i] == ' ':
    #             start = i
    #             break
    #     return end - start


assert Solution().lengthOfLastWord("   ") == 0
assert Solution().lengthOfLastWord("A   ") == 1
assert Solution().lengthOfLastWord("Hello World") == 5
