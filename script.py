from typing import List


# 1. 与46相比含有重复元素
# 2. 无序！
# 但结果不能有重复排列
# 几个问题：
# 1. 为什么不能交换了。交换打乱了顺序，而顺序是去重的保证
# 2. 什么时候发生重复
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int, visit: List):
            if i == n:
                ans.append(cur_list.copy())
                return
            for j in range(n):
                if visit[j] or (j > 0 and nums[j - 1] == nums[j] and not visit[j - 1]):
                    continue
                visit[j] = True
                cur_list[i] = nums[j]
                dfs(i + 1, visit)
                visit[j] = False

        n = len(nums)
        cur_list = [0] * n
        ans = []
        nums.sort()
        dfs(0, [False] * n)
        return ans


print(Solution().permuteUnique([1, 1, 2]))
print(Solution().permuteUnique([1, 2, 2]))
print(Solution().permuteUnique([0, 0, 2, 2, 1, 1, 1]))
