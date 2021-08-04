#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# find balanced index for an input array
# @param inputArray int整型一维数组 the input array
# @return int整型
#
class Solution:
    def findBalancedIndex(self, inputArray):
        total = sum(inputArray)
        cur = 0
        for i in range(len(inputArray)):
            num = inputArray[i]
            if cur == total - num - cur:
                return i
            cur += num


assert Solution().findBalancedIndex([1, 2, 3, 4, 6]) == 3
