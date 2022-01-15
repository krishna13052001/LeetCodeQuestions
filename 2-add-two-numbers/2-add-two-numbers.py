# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        head1 = l1
        head2 = l2
        head = res
        while(head1 or head2):
            head.val = head.val + self.addNode(head1,head2)
            if(head.val<10):
                if head1 and head1.next or head2 and head2.next:
                    head.next = ListNode(0)
            else:
                head.val -= 10
                head.next = ListNode(1)
            if(head1):
                head1 = head1.next
            if(head2):
                head2 = head2.next
            head = head.next
        return res
    
    
    def addNode(self,n1,n2):
        if(not n1 and not n2):
            raise Exception("None nodes can't be added")
        if not n1:
            return n2.val
        if not n2:
            return n1.val
        return n1.val+n2.val
        