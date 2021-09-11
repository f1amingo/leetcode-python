from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = {0: 1}
        cur = 0
        ans = 0
        for num in nums:
            cur += num
            mod = cur % k
            freq = pre.get(mod, 0)
            ans += freq
            pre[mod] = freq + 1
        return ans


print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
