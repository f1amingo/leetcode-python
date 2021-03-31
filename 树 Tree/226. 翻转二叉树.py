from collections import deque

from util.ZTree import TreeNode


class Solution:
    # 层序迭代
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stk = [root]
        while stk:
            node = stk.pop()
            node.left, node.right = node.right, node.left
            # 进入顺序无任何要求，只要处理到每一个节点即可
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return root

    # 递归
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root:
    #         # 存下来
    #         left = self.invertTree(root.left)
    #         right = self.invertTree(root.right)
    #         root.left, root.right = right, left
    #     return root
