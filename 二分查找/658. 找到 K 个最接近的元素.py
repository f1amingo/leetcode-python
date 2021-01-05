from typing import List


class Solution:
    # 双指针排除到k个元素
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[len(arr) - k:]
        lt, rt = 0, len(arr) - 1
        while rt - lt + 1 > k:
            if x - arr[lt] <= arr[rt] - x:
                rt -= 1
            else:
                lt += 1
        return arr[lt:rt + 1]


assert Solution().findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5) == [3, 3, 4]
assert Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
assert Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
