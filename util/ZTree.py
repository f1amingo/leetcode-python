from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTreeFromList(A: List) -> TreeNode:
    def build(i):
        if i >= len(A):
            return None
        if A[i]:
            _head = TreeNode(A[i])
            _head.left = build(2 * i + 1)
            _head.right = build(2 * i + 2)
            return _head

    return build(0)


def getTreeNodeWithValue(root: TreeNode, value) -> TreeNode:
    if not root:
        return root
    if root.val == value:
        return root
    node = getTreeNodeWithValue(root.left, value)
    if node:
        return node
    return getTreeNodeWithValue(root.right, value)




'''
*****0
***/***\
**1*****2
*/*\***/*\
3***4*5***6

**0
*/*\
1***2
'''
