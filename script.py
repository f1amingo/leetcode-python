# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key < root.val:
            # 左子树中删除
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # 右子树中删除
            root.right = self.deleteNode(root.right, key)
        else:
            # 删除当前节点
            if not root.left:
                # 没有左子树，返回右子树
                root = root.right
            elif not root.right:
                # 没有右子树，返回左子树
                root = root.left
            else:
                # 左右子树都存在，右子树作为新的根
                # 左子树挂到右子树中最小节点上（作为最小节点的左子树）
                min_node = root.right
                while min_node.left:
                    min_node = min_node.left
                min_node.left = root.left
                root = root.right
        return root
