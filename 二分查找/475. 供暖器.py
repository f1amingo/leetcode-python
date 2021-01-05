from typing import List


class Solution:
    # 找到离每个房屋最近的加热器
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses:
            # lo不一定是距离最近的，也可能是上一步的
            lo, hi = 0, len(heaters) - 1
            tmp = abs(house - heaters[0])
            while lo < hi:
                mid = (lo + hi) >> 1
                if heaters[mid] < house:
                    lo = mid + 1
                    tmp = min(tmp, house - heaters[mid])
                else:
                    hi = mid
                    tmp = min(tmp, heaters[mid] - house)
                    if tmp == 0:
                        break
            tmp = min(tmp, abs(house - heaters[lo]))
            ans = max(ans, tmp)
        return ans

    # 二分枚举可能的半径值，比较慢
    # def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    #     # 半径为radius时，供暖能否覆盖所有房子
    #     def coverAll(radius: int) -> bool:
    #         i, j = 0, 0
    #         while i < m and j < n:
    #             if heaters[j] - radius <= houses[i] <= heaters[j] + radius:
    #                 i += 1
    #             else:
    #                 j += 1
    #         return i == m
    #
    #     houses.sort()
    #     heaters.sort()
    #     m, n = len(houses), len(heaters)
    #     # 最小覆盖半径0，最大覆盖半径max(houses)-1
    #     lo, hi = 0, max(heaters[-1], houses[-1])
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         if coverAll(mid):
    #             hi = mid
    #         else:
    #             lo = mid + 1
    #     return lo


assert Solution().findRadius([1, 2, 3, 4], [1, 4]) == 1
assert Solution().findRadius([1], [1, 2, 3, 4]) == 0
assert Solution().findRadius([1, 5], [10]) == 9
assert Solution().findRadius([1, 5], [2]) == 3
assert Solution().findRadius([1, 2, 3], [2]) == 1
