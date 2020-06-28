class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def create_list(num):
    head = prev = ListNode(-1)
    for n in num:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head.next


def print_list(head):
    nums = []
    while head is not None:
        nums.append(head.val)
        head = head.next

    print(nums)


def reverse_list(head):
    if head is None:
        return head

    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    print_list(prev)


def reverse_between(head, m, n):
    if m == n:
        return head

    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    for _ in range(m - 1):
        prev = prev.next

    reverse = None
    curr = prev.next

    for _ in range(n - m + 1):
        temp = curr.next
        curr.next = reverse
        reverse = curr
        curr = temp

    prev.next.next = curr
    prev.next = reverse

    print_list(dummy.next)


linked_list1 = create_list([1, 2, 3, 4, 5, 6, 7])
reverse_list(linked_list1)
linked_list2 = create_list([1, 2, 3, 4, 5, 6, 7])
reverse_between(linked_list2, m=2, n=5)
