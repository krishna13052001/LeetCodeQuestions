# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for n in lists:
            cur = n
            while cur:
                heapq.heappush(heap, cur.val)
                cur = cur.next
		
        dummy = ListNode(0)
        if heap:
            newNode = ListNode(heap[0])
            dummy.next = newNode
            heapq.heappop(heap)
            cur = newNode
            while heap:
                newNode = ListNode(heap[0])
                cur.next = newNode
                cur = newNode
                heapq.heappop(heap)
                
        return dummy.next