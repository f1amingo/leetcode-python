# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    # 不使用dict来保存对应关系，无额外空间
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 1. 复制整个链表，新节点放在旧节点后
        ptr1 = head
        while ptr1:
            node = Node(ptr1.val)
            _next = ptr1.next
            ptr1.next = node
            node.next = _next
            ptr1 = _next
        # 2. 设置random指针
        ptr1 = head
        while ptr1:
            if ptr1.random:
                ptr1.next.random = ptr1.random.next
            ptr1 = ptr1.next.next
        # 3. 新旧链表拆开
        ptr1 = head
        ptr2 = dummy = Node(-1)
        while ptr1:
            new_node = ptr1.next
            ptr1.next = new_node.next
            new_node.next = None
            ptr2.next = new_node
            ptr2 = new_node
            ptr1 = ptr1.next
        return dummy.next

    # 使用一个dict来保存新旧节点对应关系
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     ptr1 = head
    #     # 使用dummy2避免判断
    #     ptr2 = dummy2 = Node(-1)
    #     # found保存原始节点N与新节点N'的对应关系
    #     found = {}
    #     # 第一步：先复制整个链表
    #     while ptr1:
    #         node = Node(ptr1.val)
    #         ptr2.next = node
    #         ptr2 = node
    #         found[ptr1] = node
    #         ptr1 = ptr1.next
    #     ptr1 = head
    #     # 第二步：设置新链表的random
    #     while ptr1:
    #         if ptr1.random:
    #             found[ptr1].random = found[ptr1.random]
    #         ptr1 = ptr1.next
    #     return dummy2.next
