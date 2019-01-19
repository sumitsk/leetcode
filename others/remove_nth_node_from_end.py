# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr = head
        ln = self.length(head)
        j = ln - n
        i = 0
        while i < j-1:
            ptr = ptr.next
            i += 1
        if j==0:
            head = head.next    
        elif j==ln:
            ptr.next = None
        else:
            ptr.next = ptr.next.next
        return head
    
    def length(self, head):
        ptr = head
        n = 0
        while ptr is not None:
            n += 1
            ptr = ptr.next
        return n