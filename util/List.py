class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def toLinkedList(A):
    ptr = dummy = ListNode(-1)
    for ele in A:
        ptr.next = ListNode(ele)
        ptr = ptr.next
    return dummy.next


def printLinkedList(head: ListNode):
    A = []
    while head:
        A.append(str(head.val))
        head = head.next
    print('[%s]' % ', '.join(A))


if __name__ == '__main__':
    test_A_1 = [1, 2, 3]
    head = toLinkedList(test_A_1)
    printLinkedList(head)
