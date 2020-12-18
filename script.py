# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPQ(r: 'TreeNode') -> (bool, bool):
            if not r:
                return False, False
            hasP, hasQ = (r.val == p.val), (r.val == q.val)
            ltP, ltQ = findPQ(r.left)
            hasP, hasQ = hasP or ltP, hasQ or ltQ
            # 左子树和当前节点已经含有P, Q
            # 则没有必要再递归右子树
            if not hasP or not hasQ:
                rtP, rtQ = findPQ(r.right)
                hasP, hasQ = hasP or rtP, hasQ or rtQ
            # 第一次同时找到P, Q，更新结果
            if hasP and hasQ:
                nonlocal ans
                if not ans:
                    ans = r
            return hasP, hasQ

        ans = None
        findPQ(root)
        return ans
