class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        size = len(s)
        i = size - 2
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1
        if i < 0:
            # 整体降序排序
            return -1
        j = size - 1
        while i < j and s[i] >= s[j]:
            j -= 1
        s[i], s[j] = s[j], s[i]
        lt, rt = i + 1, size - 1
        while lt < rt:
            s[lt], s[rt] = s[rt], s[lt]
            lt += 1
            rt -= 1
        return int(''.join(s))


assert Solution().nextGreaterElement(12222333) == 12223233
assert Solution().nextGreaterElement(11) == -1
assert Solution().nextGreaterElement(21) == -1
assert Solution().nextGreaterElement(12) == 21
