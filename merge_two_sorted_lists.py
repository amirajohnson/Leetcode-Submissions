# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current1 = list1
        current2 = list2
        h = ListNode()
        s = h

        while(current1 is not None and current2 is not None):
            if current1.val <= current2.val:
                h.next = current1
                current1 = current1.next
            else:
                h.next = current2
                current2 = current2.next
            h = h.next

        if current1 is not None:
            h.next = current1
        elif current2 is not None:
            h.next = current2
        
        return s.next
