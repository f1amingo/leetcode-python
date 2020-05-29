# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # # 递归 超越栈深度
        # ans = []
        #
        # def inorder(_root):
        #     if not root:
        #         return
        #     ans.append(root.val)
        #     inorder(root.left)
        #     inorder(root.right)
        #
        # inorder(root)
        # return ans

        # 使用栈
        ans = []
        stk = []
        cur = root
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans


print(Solution().inorderTraversal(None))
