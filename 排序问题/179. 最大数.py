from typing import List


# 继承str，重载 __lt__ 方法
class Larger(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 将int转化为上面的自定义str类Larger
        largest = ''.join(sorted(map(Larger, nums)))
        return '0' if largest[0] == '0' else largest


assert Solution().largestNumber([10, 2]) == '210'
assert Solution().largestNumber([3, 30, 34, 5, 9]) == "9534330"
assert Solution().largestNumber([1]) == "1"
