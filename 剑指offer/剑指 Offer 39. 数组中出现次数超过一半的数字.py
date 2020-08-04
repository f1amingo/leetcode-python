from typing import List


class Solution:

    # 方法三：Moore投票法
    def majorityElement(self, nums: List[int]) -> int:
        cur, votes = -1, 0
        for num in nums:
            if votes == 0:
                cur =  num
            votes += 1 if cur == num else -1
        return cur

    # 方法二：排序
    # def majorityElement(self, nums: List[int]) -> int:
    #     # 当有两个元素时，取到右边的元素
    #     # 当有一个元素时，取到自身
    #     # 所以不用加一，也不用减一
    #     return sorted(nums)[len(nums) // 2]

    # 方法一：遍历使用hash统计
    # def majorityElement(self, nums: List[int]) -> int:
    #     n, found = len(nums), {}
    #     for num in nums:
    #         found[num] = found.get(num, 0) + 1
    #         if found[num] > n // 2:
    #             return num
    #     return -1


print(Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
