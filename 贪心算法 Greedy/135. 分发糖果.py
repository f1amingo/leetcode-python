from typing import List


class Solution:

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_list = [1] * n
        # 从左到右时，一定是更新右边的数
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candy_list[i] = candy_list[i - 1] + 1
        ans = candy_list[-1]
        # 从右到左时，一定是更新左边的数
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy_list[i] = max(candy_list[i], candy_list[i + 1] + 1)
            ans += candy_list[i]
        return ans


assert Solution().candy([1, 0, 2]) == 5
