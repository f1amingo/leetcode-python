from typing import List


class Solution:
    # 文章序号为X，引用为Y，作图，寻找X=Y与图像的交点
    # 排序后线性查找
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        i = 0
        citations.sort(reverse=True)
        while i < n and citations[i] > i:
            i += 1
        return i


assert Solution().hIndex([3, 0, 6, 1, 5]) == 3
