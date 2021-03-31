import collections


class Solution:
    # 单调栈
    def removeDuplicateLetters(self, s: str) -> str:
        remain = collections.Counter(s)
        # 是否已经入栈
        visited = set()
        stk = []
        for c in s:
            # 不在栈内才处理
            if c not in visited:
                # 碰到一个更小的值，尽量把这个值往前放
                while stk and stk[-1] > c and remain[stk[-1]] > 0:
                    visited.remove(stk.pop())
                stk.append(c)
                visited.add(c)
            # 记得更新剩余次数
            remain[c] -= 1
        return ''.join(stk)


assert Solution().removeDuplicateLetters('cbacdcbc') == 'acdb'
assert Solution().removeDuplicateLetters('bcabc') == 'abc'
