# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1.左子树的所有节点值小于当前节点值
# 2.右子树的所有节点值大于当前节点值
# 3.左右子树都是BST
# 4.注意：不可含有重复值！
class Solution:
    # 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if pre >= root.val:
                return False
            pre = root.val
            root = root.right
        return True

    # BST中序遍历有序，递归
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def inOrder(node: TreeNode) -> bool:
    #         if node:
    #             lt = inOrder(node.left)
    #             nonlocal pre
    #             if not lt or pre >= node.val:  # BST不允许重复值！
    #                 return False
    #             pre = node.val  # 注意更新
    #             return inOrder(node.right)
    #         return True
    #
    #     pre = float('-inf')
    #     return inOrder(root)  # 默认返回True


r = TreeNode(2)
r.left = TreeNode(1)
r.right = TreeNode(3)
print(Solution().isValidBST(r))

r = TreeNode(5)
r.left = TreeNode(1)
right = TreeNode(4)
right.left = TreeNode(3)
right.right = TreeNode(6)
r.right = right
print(Solution().isValidBST(r))

print(Solution().isValidBST(TreeNode(1)))
