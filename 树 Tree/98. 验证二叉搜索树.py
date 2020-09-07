# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def dfs(root: TreeNode, low=float('-inf'), high=float('inf')):
    #         if not root:
    #             return True
    #         if low < root.val < high:
    #             return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
    #         return False
    #
    #     return dfs(root)

    # 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        stk = []
        cur_node = root
        pre_val = float('-inf')
        while stk or cur_node:
            while cur_node:
                stk.append(cur_node)
                cur_node = cur_node.left
            cur_node = stk.pop()
            if cur_node.val <= pre_val:
                return False
            pre_val = cur_node.val
            cur_node = cur_node.right
        return True


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
