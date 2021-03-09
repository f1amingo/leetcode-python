from util.ZTree import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 判断两棵树是否镜像对称
        def isSym(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return isSym(node1.left, node2.right) and isSym(node1.right, node2.left)

        return isSym(root, root)
