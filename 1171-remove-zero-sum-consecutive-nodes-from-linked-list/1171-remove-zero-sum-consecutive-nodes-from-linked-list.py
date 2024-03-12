# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        d = {0: dummy}
        prefixSum = 0
        while head != None:
            prefixSum += head.val
            if d.get(prefixSum, - 1) == -1:
                d[prefixSum] = head
            else:
                pf = prefixSum
                start = d[prefixSum]
                temp = start
                while temp.next != head:
                    temp = temp.next
                    pf += temp.val
                    del d[pf]
                start.next = head.next
            head = head.next
        return dummy.next
        
        