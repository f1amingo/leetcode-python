# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # res = ''
        #
        # def dfs(node):
        #     nonlocal res
        #     if node:
        #         res += str(node.val) + ','
        #         dfs(node.left)
        #         dfs(node.right)
        #     else:
        #         res += '$,'
        #
        # dfs(root)
        # return res[:-1]
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        split_list = data.split(',')
        i = 0

        def dfs():
            nonlocal i
            if i < len(split_list):
                node = None
                if split_list[i] == '$':
                    i += 1
                else:
                    node = TreeNode(split_list[i])
                    i += 1
                    node.left, node.right = dfs(), dfs()

                return node

        return dfs()


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(3)
root.right.left.right = TreeNode(1)

# Your Codec object will be instantiated and called as such:
codec = Codec()
res = codec.serialize(root)
print(res)
# new_root = codec.deserialize(res)
# print(new_root)
