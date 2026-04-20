# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        head = dummy
        head1 = list1
        head2 = list2
        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head = head1
                head1 = head1.next
                head.next = None
            else:
                head.next = head2
                head = head2
                head2 = head2.next
                head.next = None
        while head1:
            head.next = head1
            head = head1
            head1 = head1.next
            head.next = None
        while head2:
            head.next = head2
            head = head2
            head2 = head2.next
            head.next = None
        return dummy.next
