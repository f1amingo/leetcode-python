from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            self.pre_sum[i] = self.pre_sum[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if j >= i:
            return self.pre_sum[j + 1] - self.pre_sum[i]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
print(obj.sumRange(0, 0))
print(obj.sumRange(5, 5))
