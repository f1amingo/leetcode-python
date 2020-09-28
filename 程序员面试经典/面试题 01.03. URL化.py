# 这题测试用例有问题
# "ds sdfs afs sdfa dfssf asdf             " 27 这不是瞎搞？
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return '%20'.join(S[:length].split(" "))

    # def replaceSpaces(self, S: str, length: int) -> str:
    #     s_list = list(S)
    #     i, j = length - 1, len(S) - 1
    #     while i >= 0:
    #         if s_list[i] == ' ':
    #             s_list[j] = '0'
    #             j -= 1
    #             s_list[j] = '2'
    #             j -= 1
    #             s_list[j] = '%'
    #         else:
    #             s_list[j] = s_list[i]
    #         i -= 1
    #         j -= 1
    #     return ''.join(s_list)


print(Solution().replaceSpaces("ds sdfs afs sdfa dfssf asdf             ", 27))
print(Solution().replaceSpaces("Mr John Smith    ", 13))
print(Solution().replaceSpaces("               ", 5))
