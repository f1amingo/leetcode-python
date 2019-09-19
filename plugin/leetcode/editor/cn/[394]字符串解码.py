# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
#
# 示例: 
#
# 
# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
# 
# Related Topics 栈 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        for char in s:
            if char == ']':
                encoded_string = ''
                while stk[-1] != '[':
                    encoded_string = stk.pop() + encoded_string
                stk.pop()
                str_k = ''
                while stk and stk[-1].isnumeric():
                    str_k = stk.pop() + str_k
                decoded_string = ''
                for i in range(int(str_k)):
                    decoded_string += encoded_string
                stk.append(decoded_string)
            else:
                stk.append(char)
        return ''.join(stk)


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().decodeString('3[a]2[bc]'))
print(Solution().decodeString('3[a2[c]]'))
print(Solution().decodeString('2[abc]3[cd]ef'))
print(Solution().decodeString('100[leetcode]'))
