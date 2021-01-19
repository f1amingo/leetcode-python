from typing import List


# goal: 满足尽可能多的孩子
# 可以多吃，不能少吃
# 饥饿度最小最容易吃饱，先考虑饥饿度最小的孩子
class Solution:
    # LeetCode101 可读性很好
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, cookie = 0, 0
        child_size, cookie_size = len(g), len(s)
        while child < child_size and cookie < cookie_size:
            if g[child] <= s[cookie]:
                child += 1
            # 每次迭代，cookie都可以+1
            cookie += 1
        return child

    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     if not g or not s:
    #         return 0
    #     g.sort(reverse=True)
    #     s.sort(reverse=True)
    #     i = j = 0
    #     m, n = len(g), len(s)
    #     res = 0
    #     while i < m and j < n:
    #         if g[i] <= s[j]:
    #             i += 1
    #             j += 1
    #             res += 1
    #         else:
    #             i += 1
    #     return res


print(Solution().findContentChildren([1, 2], [1, 2, 3]))
print(Solution().findContentChildren([1, 2, 3], [1, 1]))
