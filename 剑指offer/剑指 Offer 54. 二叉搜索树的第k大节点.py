# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from util.ZTree import *


# BST的中序遍历有序，第k大就是中序遍历中下标为n - k的元素，k从1开始。
# 给自己看的：前序、中序居然写错了！？所谓前、中指的是根节点的位置，中序LNR。
# 困难：树的大小n提前不可知，只有遍历一遍才能知道n，但如果要把遍历结果整个保存下来，显然n - k之后都在白作功；
# 解决：但如果把中序遍历倒序变成RNL，那么只用找下标为k-1的元素，不再需要知道n，可以提前结束；
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stk, p = [], root
        while stk or p:
            # 想象一个右子树很长的树，从根开始一直到最底，逐个把节点加入栈中
            while p:
                stk.append(p)
                p = p.right
            # 现在你到最底了，没有节点了，
            # 你再从栈中取一个节点，并访问
            p = stk.pop()
            k -= 1
            if k == 0:
                return p.val
            # 访问了根节点，再看看有没有左子树
            p = p.left

    # def kthLargest(self, root: TreeNode, k: int) -> int:
    #     def inorder_traversal(r: TreeNode):
    #         if not r:
    #             return
    #         nonlocal res, count_down_k  # 从外部函数共享
    #         inorder_traversal(r.right)  # 倒序，先遍历right
    #         if count_down_k == 0:
    #             if res == -1:  # 注意，一定要确保res之前没被改过，不然会被父节点的值覆盖了
    #                 res = r.val
    #             return
    #         count_down_k -= 1
    #         inorder_traversal(r.left)
    #
    #     count_down_k = k - 1
    #     res = -1
    #     inorder_traversal(root)
    #     return res


roo = buildTreeFromList([3, 1, 4, None, 2])
print(Solution().kthLargest(roo, 1))
