class Solution:
    # 凡是数字考虑正负，凡是字母考虑大小写
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        # s_list = [x for x in s]
        s_list = list(s)  # 更简单的写法
        aeiou = {'a', 'e', 'i', 'o', 'u'}
        while i < j:
            while i < j and s[i].lower() not in aeiou:
                i += 1
            while i < j and s[j].lower() not in aeiou:
                j -= 1
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        return ''.join(s_list)


print(Solution().reverseVowels("aA"))
print(Solution().reverseVowels('hello'))
print(Solution().reverseVowels('leetcode'))
print(Solution().reverseVowels('aei'))
