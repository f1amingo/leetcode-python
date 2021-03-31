from typing import List


# 环路
# 油箱无限容量
# 任选一个加油站是否能绕一圈
class Solution:
    # 优化
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left, start, total_gas, total_cost = 0, 0, 0, 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            left += gas[i] - cost[i]
            if left < 0:
                start = i + 1
                left = 0
        return -1 if total_gas < total_cost else start

    # 暴力O(n^2)
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     # 现在位于 i ，还有 cur_gas 的油
    #     def go(i: int, cur_gas: int, step: int):
    #         if step == n:
    #             return True
    #         cur_gas += (gas[i] - cost[i])
    #         if cur_gas < 0:
    #             return False
    #         return go((i + 1) % n, cur_gas, step + 1)
    #
    #     n = len(gas)
    #     for i in range(n):
    #         if go(i, 0, 0):
    #             return i
    #     return -1


assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
