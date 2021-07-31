from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        n = len(distance)
        cur = 0
        i = start
        while i != destination:
            cur += distance[i]
            i += 1
            i %= n
        return min(cur, total - cur)


assert Solution().distanceBetweenBusStops([1, 2, 3, 4], 0, 1) == 1
assert Solution().distanceBetweenBusStops([1, 2, 3, 4], 1, 0) == 1
