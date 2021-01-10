import collections
from typing import List


class Solution:
    # 其实关心的不是每个单词的出现次数，而是它的最后出现位置
    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        n = len(S)
        # 记录每个单词的最后位置
        for i in range(n):
            last[ord(S[i]) - ord('a')] = i
        start = end = 0
        ans = []
        for i in range(n):
            end = max(end, last[ord(S[i]) - ord('a')])
            if end == i:
                ans.append(end - start + 1)
                start = end + 1  # 新的开始
        return ans

    # 滑动窗口+计数
    # def partitionLabels(self, S: str) -> List[int]:
    #     n = len(S)
    #     lt, rt = 0, 0  # 滑动窗口左右边界
    #     counter = collections.Counter(S)  # 计数
    #     cur_set = set()  # 当前窗口中含有的字母
    #     zero_count_num = 0  # 当前窗口中出现次数减为0的字母数量
    #     ans = []
    #     while rt < n:
    #         c = S[rt]
    #         counter[c] -= 1
    #         # 新字母加入当前集合
    #         if c not in cur_set:
    #             cur_set.add(c)
    #         # 出现次数减为0，该字母后面不会再出现
    #         if counter[c] == 0:
    #             zero_count_num += 1
    #         # 集合中所有字母在之后都不会出现
    #         if zero_count_num == len(cur_set):
    #             ans.append(rt - lt + 1)
    #             cur_set.clear()
    #             zero_count_num = 0
    #             lt = rt + 1  # 记得更新左边界
    #         rt += 1
    #     return ans


assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
