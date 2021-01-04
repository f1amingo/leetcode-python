# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import TreeNode


# BST中的第k小元素
# 中序遍历升序，中序遍历的第k个节点值
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cur, stk = root, []
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
