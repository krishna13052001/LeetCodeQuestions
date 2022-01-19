# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head ==None or head.next ==None):
            return None
        fast = head
        slow = head
        while(fast != None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                break
        if(fast == None or fast.next == None):
            return None
        fast = head
        while(fast!=slow):
            fast = fast.next
            slow = slow.next
        return fast 