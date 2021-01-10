from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        lt, rt = nums[0], None
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                # if t is None 和 if not t 并不等价
                if lt is None:
                    lt = nums[i]
                rt = nums[i + 1]
            else:
                ans.append(str(lt) + '->' + str(rt) if rt else str(lt))
                lt, rt = nums[i + 1], None
        ans.append(str(lt) + '->' + str(rt) if rt else str(lt))
        return ans


assert Solution().summaryRanges([0]) == ['0']
assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
assert Solution().summaryRanges([]) == []
assert Solution().summaryRanges([-1]) == ['-1']
