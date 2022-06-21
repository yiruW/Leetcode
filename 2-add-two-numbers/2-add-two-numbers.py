# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = str(l1.val)
        b = str(l2.val)
        
        next = l1.next
        while next:
            a = str(next.val) + a
            next = next.next
        
        next = l2.next
        while next:
            b = str(next.val) + b
            next = next.next
        
        c = str(int(a) + int(b))
        i = len(c) - 1
        l3 = ListNode(int(c[i]))
        next = l3
        
        while i > 0:
            i -= 1
            print(i)
            ch = int(c[i])
            if next != None:
                next.next = ListNode(ch)
                next = next.next
                
        return l3