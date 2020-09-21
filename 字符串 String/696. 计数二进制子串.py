class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        ptr = last = res = 0
        while ptr < n:
            count = 0
            # 把字符保存下来，世界都变得容易了
            c = s[ptr]
            while ptr < n and s[ptr] == c:
                ptr += 1
                count += 1
            res += min(count, last)
            last = count
        return res

print(
    Solution().countBinarySubstrings("01")
)
