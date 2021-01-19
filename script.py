from typing import List


# goal: 满足尽可能多的孩子
# 可以多吃，不能少吃
# 饥饿度最小最容易吃饱，先考虑饥饿度最小的孩子
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, cookie = 0, 0
        child_size, cookie_size = len(g), len(s)
        while child < child_size and cookie < cookie_size:
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


assert Solution().findContentChildren([1, 2, 3], [1, 1]) == 1
