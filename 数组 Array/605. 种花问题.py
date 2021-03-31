from typing import List


# 两朵花不能相邻
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True
        return False


assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1)
assert not Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2)
assert Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0)
