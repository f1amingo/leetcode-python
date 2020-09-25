from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        n = len(chars)
        while j < n:
            chars[i] = chars[j]
            j += 1
            count = 1
            # j移到区块末尾+1的位置
            # 统计相同字母数量
            while j < n and chars[j] == chars[j - 1]:
                j += 1
                count += 1
            i += 1
            start = i
            if count == 1:
                continue
            # 字母数量写回 从低位到高位
            while count:
                count, chars[i] = divmod(count, 10)
                chars[i] = str(chars[i])
                i += 1
            end = i - 1
            # reverse
            while start < end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1
        return i


assert Solution().compress(["a"]) == 1
assert Solution().compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
assert Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
