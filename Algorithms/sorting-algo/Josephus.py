# 问题描述：编号为 1-N 的 N 个士兵围坐在一起形成一个圆圈，
# 从编号为 1 的士兵开始依次报数（1，2，3…这样依次报），
# 数到 m 的 士兵会被杀死出列，之后的士兵再从 1 开始报数。
# 直到最后剩下一士兵，求这个士兵的编号。


# recursive
def f(n, m, i):
    if i == 1:
        return (n + m - 1) % n
    return (f(n - 1, m, i - 1) + m) % n


n = 6
m = 3
for i in range(1, n + 1):
    print('{}th: {}'.format(i, f(n, m, i)))


# linkedlist

# class ListNode(object):
#
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# def create_list(nums):
#     head = ListNode(nums[0])
#     prev = head
#     for i in nums[1:]:
#         node = ListNode(i)
#         prev.next = node
#         prev = node
#
#     prev.next = head
#     return head
#
# def print_list(head):
#     ans = []
#     while head is not None:
#         val = head.val
#         if val not in ans:
#             ans.append(val)
#             head = head.next
#         else:
#             break
#     print(ans)
#
#
# def solve(n, m):
#     head = create_list([i for i in range(n)])
#     # print_list(head)
#     count = 1
#     curr = head
#     prev = None
#     c = n-1
#     while head.next != head:
#         if count == m:
#             count = 1
#             print('delete: ', curr.val)
#             prev.next = curr.next
#             curr = prev.next
#             c -= 1
#             if c == 0:
#                 break
#         else:
#             count += 1
#             prev = curr
#             curr = curr.next
#
#
#     print('remain: ', head.val)
#
# solve(10, 3)




