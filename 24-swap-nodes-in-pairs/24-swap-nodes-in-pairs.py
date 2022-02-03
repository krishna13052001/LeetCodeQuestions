# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        node = head
        prev = None
        nnode = head.next
        start = head
        while(node != None and nnode != None):
            if(prev == None):
                # print(node.val,nnode.val,node.next,nnode.next)
                node.next = nnode.next
                nnode.next = node
                # print(node.val,nnode.val,nnode.next)
                prev = node
                start = nnode  
            else:
                prev.next = nnode
                node.next = nnode.next
                nnode.next = node
                prev = node
            node = prev.next
            if(node != None):
                nnode = node.next
        return start
            