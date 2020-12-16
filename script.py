class Solution:
    def decodeString(self, s: str) -> str:
        stk, res, times = [], '', 0
        for c in s:
            if c == '[':
                stk.append((res, times))
                res, times = '', 0
            elif c == ']':
                # 不要覆盖原times
                last_res, last_times = stk.pop()
                res = last_res + last_times * res
            elif '0' <= c <= '9':
                times = times * 10 + int(c)
            else:
                res += c
        return res


assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
assert Solution().decodeString("3[a2[c]]") == "accaccacc"
assert Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
