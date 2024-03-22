# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        slow = head
        fast = head
        while fast != None and fast.next != None:
            s.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        if fast !=None and fast.next == None:
            slow = slow.next
        print(s, fast)
        while len(s) > 0 and slow != None:
            ele = s.pop()
            if ele != slow.val:
                return False
            slow = slow.next
        return True