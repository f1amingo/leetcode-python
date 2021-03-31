"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 对 this_node 进行拷贝
        def dfs(this_node: 'Node'):
            if this_node.val in node_map:
                return
            new_node = Node(this_node.val)
            node_map[this_node.val] = new_node
            for neighbor in this_node.neighbors:
                # 确保邻居已经被拷贝
                dfs(neighbor)
                new_node.neighbors.append(node_map[neighbor.val])

        if not node:
            return node
        node_map = {}
        dfs(node)
        return node_map[node.val]
