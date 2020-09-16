from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dict_len在一段连续区间的左右端点保存了区间长度
        # 因为区间只能拼接到左边或者右边，所以只用在区间两端记录长度
        dict_len, max_len = {}, 0
        for num in nums:
            if num not in dict_len:
                left, right = dict_len.get(num - 1, 0), dict_len.get(num + 1, 0)
                cur_len = left + right + 1
                max_len = max(max_len, cur_len)
                # 不可以省略dict_len[num]，比如[1,2,3] 4 [5,6]的情况,4连接了两个区间
                # 此时不光要设置dict[1]=dict[6]=6，也要把4加入到dict中，虽然dict[4]的值对结果无影响
                # dict_len[num - left] = dict_len[num + right] = cur_len
                dict_len[num] = dict_len[num - left] = dict_len[num + right] = cur_len
        return max_len


print(Solution().longestConsecutive([4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3]))
