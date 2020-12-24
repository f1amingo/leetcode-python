from typing import List


# 下一个排列，字典序
# 不存在下一个排序，则给出最小排列
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        flag = False
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                flag = True
                break
        # 整体降序，没有下一个更大排列
        if not flag:
            nums.reverse()
            return
        # 从i往后，找到第一个恰好大于nums[i]的数
        t = i + 1
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                if nums[j] < nums[t]:
                    t = j
        nums[i], nums[t] = nums[t], nums[i]
        nums[i + 1:] = sorted(nums[i + 1:])


nums = [1,3,2]
Solution().nextPermutation(nums)
print(nums)
