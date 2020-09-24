class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        rows = ['' for i in range(numRows)]
        i, flag = 0, 1
        # 遍历l字符串
        for c in s:
            rows[i] += c
            i += flag
            if i == 0 or i == numRows - 1:
                flag = -flag
        return ''.join(rows)

    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows < 2:
    #         return s
    #     rows = ['' for i in range(numRows)]
    #     row_idx, flag = 0, 1
    #     for i in range(len(s)):
    #         rows[row_idx] += s[i]
    #         # flag先加，和先取负顺序，如何考虑
    #         row_idx += flag
    #         if row_idx == numRows - 1 or row_idx == 0:
    #             flag = -flag
    #     return ''.join(rows)


print(Solution().convert('LEETCODEISHIRING', 2))
