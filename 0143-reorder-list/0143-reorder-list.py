# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        temp = head
        while temp != None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        isFront = True
        while temp != None:
            if isFront:
                temp.val = stack.pop(0)
                isFront = False
            else:
                temp.val = stack.pop()
                isFront = True
            temp = temp.next
            