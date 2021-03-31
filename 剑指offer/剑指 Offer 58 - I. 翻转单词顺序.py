# 翻转单词，而不是字符，空格分隔
# 1.移除前后的多余空格
# 2.单词之间也可能有多空格
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        start, end = 0, len(s) - 1
        ans = []
        while start <= end:
            # 倒序找到第一个非空字符
            rt = end
            while start <= rt and s[rt] == ' ':
                rt -= 1
            # 到头了
            if rt < start:
                break
            # 继续从rt开始找到第一个空格
            lt = rt - 1
            while start <= lt and s[lt] != ' ':
                lt -= 1
            ans.append(s[lt + 1:rt + 1])
            end = lt - 1  # lt是空格
        return ' '.join(ans)


assert Solution().reverseWords("the sky is blue") == "blue is sky the"
assert Solution().reverseWords("  hello world!  ") == "world! hello"
assert Solution().reverseWords("a good   example") == "example good a"
