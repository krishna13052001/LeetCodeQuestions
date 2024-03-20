# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node1 = node2 = None
        temp = list1
        count = 0
        while temp != None:
            if count == a-1:
                node1 = temp
            elif count == b:
                node2 = temp.next
                break
            temp = temp.next
            count += 1
        if True:
            temp = list2
            while temp.next != None:
                temp = temp.next
            node1.next = list2
            temp.next = node2
        return list1
        