# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1. 终止条件：递归和迭代何时停止？聚焦在当前操作节点
# 边界条件：cur指向head和tail时如何操作？
# 2. 初始化：迭代需要声明哪些变量？
# 3. 如何反转当前节点：反转对于一个节点意味着什么？
# 4. 返回值：哪个才是反转后的新头结点？
class Solution:
    # 递归
    # def reverseList(self, head: ListNode) -> ListNode:
    #     # 初始化：pre为前一个节点，cur为后一个节点
    #     # 所有操作均从cur的出发
    #     # 原本的head反转后变成tail，tail.next应该为None，因此pre初始为None
    #     pre, cur = None, head
    #     # cur先到尾部，循环体内必须保证cur不为空
    #     while cur:
    #         # 为了反转cur需要指向pre，这样会把本来的cur.next丢弃，导致链表断开，因此需要保存cur.next
    #         next = cur.next
    #         # 反转整个链表，只需要逐个节点反转
    #         # 对于cur这一个节点而言，反转就是指向前一个节点(pre)，而不再是后一个节点(next)
    #         cur.next = pre
    #         # pre, cur都往前走一步，准备下一轮迭代
    #         pre, cur = cur, next
    #     # 循环能结束说cur一定为None，如果再返回cur，脑子秀逗了？
    #     return pre

    # 递归
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归终止条件：head为空，或者只有一个节点显然不需要反转
        if not (head and head.next):
            return head
        # 对于当前节点head，首先反转之后的部分(head.next)
        # 返回值re_head是反转后的头结点
        re_head = self.reverseList(head.next)
        # 实际对当前节点head进行反转，让下一个节点指向自己，然后自己指向None
        # 为什么自己可以指向None？因为此时之后的部分已经被反转了，不再需要被访问
        head.next.next = head  # 这里老是写不出来！！！
        head.next = None
        # 返回头结点，可以看到头结点在整个调用栈中，被层层传递
        return re_head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node = Solution().reverseList(node1)

while node:
    print(node.val)
    node = node.next
