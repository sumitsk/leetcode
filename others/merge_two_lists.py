# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # special cases
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        p = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        while l1 is not None:
            p.next = l1
            l1 = l1.next
            p = p.next
        while l2 is not None:
            p.next = l2
            l2 = l2.next
            p = p.next
        return head