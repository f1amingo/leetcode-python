# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *
from util.List import *


class Solution:
    # 2020-9-14 13:55:13
    # 这类自己递归，再加一个子递归的题，还要加强
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(h: ListNode, r: TreeNode) -> bool:
            if not h:  # 链表走完了
                return True
            if not r:
                return False
            if h.val == r.val:
                return dfs(h.next, r.left) or dfs(h.next, r.right)
            # return dfs(h, r.left) or dfs(h, r.right) 这里不用再往下走了
            return False

        if not root:
            return False
        # 注意这里递归又调用了isSubPath()自身
        # return dfs(head, root) or dfs(head, root.left) or dfs(head, root.right)
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
