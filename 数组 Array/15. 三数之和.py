from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n - 1):
            # 提前结束
            if nums[i] > 0:
                break
            # 跳过重复，注意要和i-1比较，而不能比较i+1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lt, rt = i + 1, n - 1
            while lt < rt:
                this_sum = nums[i] + nums[lt] + nums[rt]
                # 注意这里三个if的写法
                if this_sum == 0:
                    # 等的时候，不能跳出循环
                    res.append([nums[i], nums[lt], nums[rt]])
                if this_sum <= 0:
                    # 小了，lt右移，找到下一个不同的数
                    while lt < rt and nums[lt] == nums[lt + 1]:
                        lt += 1
                    lt += 1
                if this_sum >= 0:
                    while lt < rt and nums[rt] == nums[rt - 1]:
                        rt -= 1
                    rt -= 1
        return res

    # L,i,R的策略不对
    # 原因在于[L]+[R]==0时，不知道该移动哪一边
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     if n < 3:
    #         return []
    #     nums.sort()
    #     res = []
    #     lt, rt = 0, len(nums) - 1
    #     while lt < rt:
    #         this_sum = nums[lt] + nums[rt]
    #         for i in range(lt + 1, rt):
    #             if this_sum + nums[i] == 0:
    #                 res.append([nums[lt], nums[i], nums[rt]])
    #                 break
    #         if this_sum >= 0:
    #             rt -= 1
    #             while rt < lt and nums[rt] == nums[rt + 1]:
    #                 rt -= 1
    #         if this_sum <= 0:
    #             lt += 1
    #             while lt < rt and nums[lt] == nums[lt - 1]:
    #                 lt += 1
    #
    #     return res


print(Solution().threeSum([0, 0, 0, 0]))
# print(Solution().threeSum([-2, 0, 1, 1, 2]))
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
