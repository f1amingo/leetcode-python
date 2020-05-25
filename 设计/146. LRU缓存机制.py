class DNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head, self.tail = DNode(-1, -1), DNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._move_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self._move_front(node)
        else:
            # 最末元素只能通过双向链表获取
            # 节点要同时保存key和value，否则不能在dict中删除自己
            if len(self.dict) == self.capacity:
                last_node = self.tail.prev
                self._remove_from_list(last_node)
                del self.dict[last_node.key]
                # self.dict.pop(last_node, key)
            node = DNode(key, value)
            self._add_to_list(node)
            self.dict[key] = node

    def _add_to_list(self, node: DNode):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def _remove_from_list(self, node: DNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = node.prev = None

    def _move_front(self, node: DNode):
        self._remove_from_list(node)
        self._add_to_list(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
