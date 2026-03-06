# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        self.length = 0
        temp = head
        tail = None
        while temp:
            self.length += 1
            tail = temp
            temp = temp.next
        tail.next = head
        temp = head
        k = k % self.length
        for _ in range(self.length - k):
            tail = temp
            temp = temp.next
        tail.next = None
        return temp