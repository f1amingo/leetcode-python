from typing import List


# 下一个排列，字典序
# 不存在下一个排序，则给出最小排列
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 找到第一个升序对
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # 逆序寻找第一个大于A[i]的元素
            j = len(nums) - 1
            while j > i and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # A[i+1:]是升序
        lt, rt = i + 1, len(nums) - 1
        while lt < rt:
            nums[lt], nums[rt] = nums[rt], nums[lt]
            lt += 1
            rt -= 1

    # 思路大体没问题，但忽略了一个重要信息，后半段是有降序的
    # def nextPermutation(self, nums: List[int]) -> None:
    #     n = len(nums)
    #     flag = False
    #     # 1.倒序找到A[i] < A[i+1]，
    #     # 此时至少可以把A[i+1]换到前面使得整体更大
    #     for i in range(n - 2, -1, -1):
    #         if nums[i] < nums[i + 1]:
    #             flag = True
    #             break
    #     # 整体降序，没有下一个更大排列
    #     if not flag:
    #         nums.reverse()
    #         return
    #     # 2.从i往后，找到第一个恰好大于A[i]的数，换到前面
    #     t = i + 1
    #     for j in range(i + 1, n):
    #         if nums[j] > nums[i]:
    #             if nums[j] < nums[t]:
    #                 t = j
    #     nums[i], nums[t] = nums[t], nums[i]
    #     # 3.对A[i]之后的部分排序，使其最小
    #     nums[i + 1:] = sorted(nums[i + 1:])


nums = [1, 3, 2]
Solution().nextPermutation(nums)
print(nums)
