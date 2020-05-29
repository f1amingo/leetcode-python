class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def buildNodeList(arr):
    head_ptr = None
    last_ptr = None
    for i in arr:
        if head_ptr is None:
            head_ptr = ListNode(i)
            last_ptr = head_ptr
        else:
            last_ptr.next = ListNode(i)
            last_ptr = last_ptr.next
    return head_ptr


def printNodeList(node):
    ptr = node
    while ptr is not None:
        print(ptr.val)
        ptr = ptr.next
