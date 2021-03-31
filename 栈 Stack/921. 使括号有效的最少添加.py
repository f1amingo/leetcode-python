class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        lt = rt = 0
        ans = 0
        for c in S:
            if c == '(':
                # 遇到'('，但之前的')'多于'('
                # 需要为之前多的')'补充'('
                # 然后重置计数
                if lt < rt:
                    ans += rt - lt
                    lt = rt = 0
                lt += 1
            else:
                rt += 1
        return ans + abs(lt - rt)


assert Solution().minAddToMakeValid('())') == 1
assert Solution().minAddToMakeValid('(((') == 3
assert Solution().minAddToMakeValid('()') == 0
assert Solution().minAddToMakeValid('()))((') == 4
