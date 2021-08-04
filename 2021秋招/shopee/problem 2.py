#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param inxml string字符串 xml字符串
# @param path string字符串 取值路径
# @return string字符串
#
class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}


class Solution:
    def GetXMLValue(self, inxml, path):
        root = Node(-1)

        # 首先解析成一棵树
        def parseTree():
            token = ''
            isEnd = False
            for ch in inxml:
                if ch == '<':
                    token = ''
                # elif ch == '>':
