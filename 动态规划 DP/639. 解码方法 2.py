# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if not s or s[0] == '0':
#             return 0
#         n = len(s)
#         pre, cur = 1, 1
#         for i in range(1, n):
#             tmp = 0
#             if s[i] == '0':
#                 if s[i - 1] == 1 or s[i - 1] == 2:
#                     tmp = pre
#                 elif s[i - 1] == '*':
#                     tmp = 2 * pre
#                 else:
#                     return 0
#             elif s[i] == '*':
#                 tmp = 9 * cur
#                 if s[i - 1] == '1':
#                     tmp += 9 * pre
#                 elif s[i - 1] == '2':
#                     tmp += 6 * pre
#                 elif s[i - 1] == '*':
#                     tmp += 15 * pre
#             # s[i]为1...9
#             elif s[i - 1] == '0':
#                 tmp = cur
#             elif s[i - 1] == '*':
#                 if s[i]
#
#         return cur
