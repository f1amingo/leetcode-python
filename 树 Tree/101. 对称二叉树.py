# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # My solution
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def isTwoTreeSymmetric(tree1: TreeNode, tree2: TreeNode):
    #         if tree1 and not tree2:
    #             return False
    #         if not tree1 and tree2:
    #             return False
    #         if not tree1 and not tree2:
    #             return True
    #         if tree1.val != tree2.val:
    #             return False
    #         outer = isTwoTreeSymmetric(tree1.left, tree2.right)
    #         inner = isTwoTreeSymmetric(tree1.right, tree2.left)
    #         return outer and inner
    #
    #     if not root:
    #         return True
    #     return isTwoTreeSymmetric(root.left, root.right)

    # 官方
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def check(p: TreeNode, q: TreeNode):
    #         # 都为空
    #         if not p and not q:
    #             return True
    #         # 有一为空
    #         if not p or not q:
    #             return False
    #         # 三个要求：根相同、左子树对称、右子树对称
    #         return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
    #
    #     # 学习一下root, root的写法
    #     return check(root, root)

    # 层序遍历
    def isSymmetric(self, root: TreeNode) -> bool:
        arr = [root]
        while arr:
            next_arr = []
            for node in arr:
                if node:
                    next_arr.append(node.left)
                    next_arr.append(node.right)
            arr = next_arr
            for i in range(len(arr) // 2):
                j = len(arr) - i - 1
                if not arr[i] and not arr[j]:
                    continue
                if not arr[i] or not arr[j]:
                    return False
                if arr[i].val != arr[j].val:
                    return False
        return True


root = TreeNode(1)
left = TreeNode(2)
left.left = TreeNode(3)
left.right = TreeNode(4)
right = TreeNode(2)
right.left = TreeNode(4)
right.right = TreeNode(3)
root.left = left
root.right = right
print(Solution().isSymmetric(root))
