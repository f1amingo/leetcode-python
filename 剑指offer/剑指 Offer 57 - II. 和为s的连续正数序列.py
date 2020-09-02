from typing import List


class Solution:
    # 双指针
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target <= 2:
            return []
        include_bound, res = (target + 1) // 2, []
        cnt_sum = right = 0
        left = 1
        while right <= include_bound:
            if cnt_sum < target:
                right += 1
                cnt_sum += right
            elif cnt_sum > target:
                cnt_sum -= left
                left += 1
            else:
                res.append([i for i in range(left, right+1)])
                cnt_sum -= left
                left += 1

        return res


print(Solution().findContinuousSequence(15))
