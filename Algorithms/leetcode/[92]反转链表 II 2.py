# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        for i in range(m-1):
            prev = prev.next

        reverse = None
        curr = prev.next
        for _ in range(n-m+1):
            temp = curr.next
            curr.next = reverse
            reverse = curr
            curr = temp

        prev.next.next = curr
        prev.next = reverse

        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
