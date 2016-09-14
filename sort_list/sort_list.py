# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        fast = head
        slow = head
        while (fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        # now slow should be in the middle
        fast = slow.next
        slow.next = None
        head = self.sortList(head)
        fast = self.sortList(fast)
        return self.merge(head, fast)
    
    def merge(self, left, right):
        if not left: return right
        if not right: return left
        dummy = ListNode('magic')
        cur = dummy
        while (left and right):
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left: # pickup leftover
            cur.next = left
        elif right: #pickup leftover
            cur.next = right
        print(dummy.next.val)
        return dummy.next
